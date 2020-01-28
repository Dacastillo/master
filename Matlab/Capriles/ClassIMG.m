classdef ClassIMG < handle
    properties
        h
        s
    end
    methods
        function start (obj)
            global Gstop
            daq.reset; obj.s = daq.createSession('ni');
            co0 = addAnalogOutputChannel(obj.s, 'LAB', 'ao0', 'Voltage');
            co1 = addAnalogOutputChannel(obj.s, 'LAB', 'ao1', 'Voltage');
            addAnalogInputChannel(obj.s,'LAB', 0, 'Voltage'); addCounterInputChannel(obj.s,'LAB', 0, 'EdgeCount');
            Gstop = 1;
        end
        
        function Image(obj)
            global arc datax_A datay_A Gstop
            X1_A = str2double(get(obj.h.xce,'string')); Y1_A =  str2double(get(obj.h.yce,'string'));
            DX_A = str2double(get(obj.h.dex,'string')); DY_A =  str2double(get(obj.h.dey,'string'));
            N_A1 = str2double(get(obj.h.dot,'string')); N_A = int64(N_A1);
            tpause1_A = str2double(get(obj.h.tef,'string'));
            Tiempo_int = str2double(get(obj.h.tin,'string'));
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            if or(or(((X1_A + DX_A*0.5)> 80), ((X1_A - DX_A*0.5)< 0)),or(((Y1_A + DY_A*0.5)> 80), ((Y1_A - DY_A*0.5)< 0))) return; end
            
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            
            ax=1:1:N_A;
            b=1:1:N_A;
            arc= 1;
            obj.s.Rate=1000;
            
            datax = linspace((X1_A/8)-(DX_A/16),(X1_A/8)+(DX_A/16),N_A)';
            datay = linspace((Y1_A/8)-(DY_A/16),(Y1_A/8)+(DY_A/16),N_A)';
            paso = (datax(2)-datax(1))*8;
            
            datax_A = ones(1,round(N_A*Tiempo_int))*datax(1);
            datay_A = ones(1,round(N_A*Tiempo_int))*datay(1);
            queueOutputData(obj.s,[datax_A'  datay_A']);
            A_zeros = 0;
            a=ones(N_A);
            [data, time] = obj.s.startForeground();
            A_data = data(:,2);
            A_zeros = A_data(end);
            a = a *A_zeros/time(end);
            for i = 1:N_A
                for j = 1:N_A
                    pause(tpause1_A/1000);
                    datax_A = ones(1,round(N_A*Tiempo_int))*datax(i);
                    datay_A = ones(1,round(N_A*Tiempo_int))*datay(j);
                    queueOutputData(obj.s,[datax_A' datay_A']);
                    input(i,j,a,b,paso);
                    stop(obj.s)
                    if not(and(arc,Gstop)); break; end
                    drawnow();
                end
                if not(and(arc,Gstop)); break; end
            end
            
            function input(x,y,vec1,vec2,paso)
                [data, time] = obj.s.startForeground();
                A_data = data(2:end,2);
                A_time = time(2:end);
                A_vect = A_data./A_time;
                A_zeros = mean(A_vect);
                Int_time = time(end);
                cnt=A_zeros;
                vec1(x,y)= cnt;
                vec2(y)= cnt;
                std_A_zeros = std(A_vect);
                h = pcolor(obj.h.axes10,8*datax,8*datax,vec1); set(h, 'EdgeColor', 'none');
                colorbar(obj.h.axes10)
                colormap(obj.h.axes10,'jet')
                plot(obj.h.axes11,8*datax,vec2)
                a=vec1; b=vec2;
                set(obj.h.cux,'String',num2str(round(8*datax(x),3)));
                set(obj.h.cuy,'String',num2str(round(8*datay(y),3)));
                set(obj.h.cnt,'String', round(cnt));
                set(obj.h.tiempo_integracion,'String', 1000*Int_time);
                set(obj.h.scn,'String', round(std_A_zeros));
                set(obj.h.stp,'String', paso*1000);
            end
            if not(Gstop); Gstop = 2; obj.StopProgram(); end
        end
        
        function Trace(obj)
            global arct Gstop;
            import java.awt.Robot;
            import java.awt.event.*;
            mouse = Robot;
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            CurrentX = str2double(get(obj.h.cux,'string'));
            CurrentY = str2double(get(obj.h.cuy,'string'));
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            X1_A = str2double(get(obj.h.xce,'string')); Y1_A =  str2double(get(obj.h.yce,'string'));
            DX_A = str2double(get(obj.h.dex,'string')); DY_A =  str2double(get(obj.h.dey,'string'));
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            cnt=0;
            arct=1;
            Trace_lenght = 25;
            cnt=1:Trace_lenght;
            ene=0;
            alltrace = 0;
            row = 0;
            xcen=CurrentX/8;
            ycen=CurrentY/8;
            while and(arct==1, Gstop==1)
                N_A1 = str2double(get(obj.h.dot,'string'));
                N_A = int64(N_A1);
                Tiempo_int = str2double(get(obj.h.tin,'string'));
                datx_A = ones(1,round(N_A*Tiempo_int))*xcen;
                daty_A = ones(1,round(N_A*Tiempo_int))*ycen;    
                row = row+1;
                ene=ene+1;
                queueOutputData(obj.s,[datx_A' daty_A']);
                [data, time] = obj.s.startForeground();
                A_data = data(2:end,2);
                A_time = time (2:end);
                A_vect = A_data./A_time;
                cnt(ene)=mean(A_vect);
                alltrace = [alltrace cnt(ene)];
                Int_time = time(end);
                if ene == Trace_lenght ene = 0; end
                if row >= Trace_lenght
                    cntaverage = mean(cnt);
                    cntstd = std(cnt);
                    set(obj.h.meancounts,'string',round(cntaverage));
                    set(obj.h.stdcounts,'string',round(cntstd));
                end
                set(obj.h.tiempo_integracion,'String', 1000*Int_time);
                plot(obj.h.axes12,cnt(1:Trace_lenght));
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                
                cumouse = get(obj.h.axes10, 'CurrentPoint');
                Xcupos = cumouse(1);
                Ycupos = cumouse (3);
                if and(Xcupos>(X1_A-(DX_A/2)), Xcupos<(X1_A+(DX_A/2))) && and(Ycupos>(Y1_A-(DY_A/2)), Ycupos<(Y1_A+(DY_A/2)))
                    mouse.mousePress(InputEvent.BUTTON3_MASK);
                    mouse.mouseRelease(InputEvent.BUTTON3_MASK);
                    xcen = Xcupos/8;
                    ycen = Ycupos/8;
                end
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                set(obj.h.cux,'String',num2str(round(8*xcen,3)));
                set(obj.h.cuy,'String',num2str(round(8*ycen,3)));
                drawnow;
                if not(Gstop); Gstop = 2; obj.StopProgram(); end
            end
        end
        function Stop(obj)
            global arc
            arc=0;
        end
        function StopTrace(obj)
            global arct
            arct=0;
        end
        
        function StopProgram (obj)
            global Gstop
            if Gstop == 2
                CurrentX = str2double(get(obj.h.cux,'string'))/8;
                CurrentY = str2double(get(obj.h.cuy,'string'))/8;
                datax = 0:CurrentX/10:CurrentX;
                datay = 0:CurrentY/10:CurrentY;
                datax = flip(datax);
                datay = flip(datay);
                if CurrentX == 0; datax = zeros(1,length(datay)); end
                if CurrentY == 0; datay = zeros(1,length(datay)); end
                for i = 1:max(size(datax))
                    datax_A = ones(1,5)*datax(i);
                    datay_A = ones(1,5)*datay(i);
                    queueOutputData(obj.s,[datax_A' datay_A']);
                    obj.s.startForeground();
                    set(obj.h.cux,'String',num2str(round(8*datax(i),3)));
                    set(obj.h.cuy,'String',num2str(round(8*datay(i),3)));
                end
                clc
                clear all
                close all
            end
            Gstop = 0;
        end
        
                

            
    end
end