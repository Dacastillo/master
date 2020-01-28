classdef ClassIMG < handle
    properties
        h
        s
    end
    methods
        function start (obj)
            daq.reset; obj.s = daq.createSession('ni');
            co0 = addAnalogOutputChannel(obj.s, 'LAB', 'ao0', 'Voltage');
            co1 = addAnalogOutputChannel(obj.s, 'LAB', 'ao1', 'Voltage');
            addAnalogInputChannel(obj.s,'LAB', 0, 'Voltage'); addCounterInputChannel(obj.s,'LAB', 0, 'EdgeCount');
        end
        function Image(obj)
            global arc datax_A datay_A
            X1_A = str2double(get(obj.h.xce,'string')); Y1_A =  str2double(get(obj.h.yce,'string'));
            DX_A = str2double(get(obj.h.dex,'string')); DY_A =  str2double(get(obj.h.dey,'string'));
            N_A1 = str2double(get(obj.h.dot,'string')); N_A = int64(N_A1);
            tpause1_A = str2double(get(obj.h.tef,'string')); Tiempo_int = str2double(get(obj.h.tin,'string'));
            if or(or(((X1_A + DX_A*0.5)> 80), ((X1_A - DX_A*0.5)< 0)),or(((Y1_A + DY_A*0.5)> 80), ((Y1_A - DY_A*0.5)< 0))) return; end
            ax=1:1:N_A;b=1:1:N_A; arc= 1; obj.s.Rate=1000; paso = (datax(2)-datax(1))*8;
            datax = linspace((X1_A/8)-(DX_A/16),(X1_A/8)+(DX_A/16),N_A)'; datay = linspace((Y1_A/8)-(DY_A/16),(Y1_A/8)+(DY_A/16),N_A)';
            datax_A = ones(1,round(N_A*Tiempo_int))*datax(1); datay_A = ones(1,round(N_A*Tiempo_int))*datay(1);
            queueOutputData(obj.s,[datax_A'  datay_A']);A_zeros = 0; a=ones(N_A);[data, time] = obj.s.startForeground(); A_data = data(:,2); A_zeros = A_data(end); a = a *A_zeros/time(end);
            for i = 1:N_A
                for j = 1:N_A
                    pause(tpause1_A/1000);datax_A = ones(1,round(N_A*Tiempo_int))*datax(i); datay_A = ones(1,round(N_A*Tiempo_int))*datay(j); queueOutputData(obj.s,[datax_A' datay_A']); input(i,j,a,b,paso); stop(obj.s)
                    if(arc==0)break; end
                    drawnow();
                end
                if(arc==0) break; end
            end
            function input(x,y,vec1,vec2,paso)
                [data, time] = obj.s.startForeground(); A_data = data(2:end,2); A_time = time(2:end); A_vect = A_data./A_time;
                A_zeros = mean(A_vect); Int_time = time(end);cnt=A_zeros; vec1(x,y)= cnt; vec2(y)= cnt; std_A_zeros = std(A_vect);
                h = pcolor(obj.h.axes10,8*datax,8*datax,vec1); set(h, 'EdgeColor', 'none');
                colorbar(obj.h.axes10)
                colormap(obj.h.axes10,'jet')
                plot(obj.h.axes11,8*datax,vec2)
                a=vec1; b=vec2; set(obj.h.cux,'String',num2str(round(8*datax(x),3))); set(obj.h.cuy,'String',num2str(round(8*datay(y),3))); set(obj.h.cnt,'String', round(cnt));
                set(obj.h.tin,'String', 1000*Int_time); set(obj.h.scn,'String', round(std_A_zeros)); set(obj.h.stp,'String', paso*1000);
            end
        end
        function Trace(obj)
            global arct datax_A datay_A; cnt=0; arct=1; Trace_lenght = 25; cnt=1:Trace_lenght; ene=0; alltrace = 0; row = 0; 
            xcen=datax_A(1); ycen=datay_A(1); 
            while arct==1
                N_A1 = str2double(get(obj.h.dot,'string')); N_A = int64(N_A1); Tiempo_int = str2double(get(obj.h.tin,'string'));  
                datx_A = ones(1,round(N_A*Tiempo_int))*xcen/8; daty_A = ones(1,round(N_A*Tiempo_int))*ycen/8;
                row = row+1; ene=ene+1; queueOutputData(obj.s,[datx_A' daty_A']); [xcen,ycen]= gpos(obj.h.axes10); 
                [data, time] = obj.s.startForeground(); A_data = data(2:end,2); A_time = time (2:end); A_vect = A_data./A_time; cnt(ene)=mean(A_vect); alltrace = [alltrace cnt(ene)];
                Int_time = time(end);
                if ene == Trace_lenght ene = 0; end
                if row >= Trace_lenght
                    cntaverage = mean(cnt); cntstd = std(cnt); set(obj.h.meancounts,'string',round(cntaverage)); set(obj.h.stdcounts,'string',round(cntstd));
                end
                set(obj.h.tim,'String', 1000*Int_time); plot(obj.h.axes12,cnt(1:Trace_lenght))
                drawnow;                
            end    
        end        
        function Stop(obj)
            global arc
            stop(obj.s);
            arc=0;
        end
        function StopTrace(obj)
            global arct
            stop(obj.s);
            arct=0;
        end
    end
end