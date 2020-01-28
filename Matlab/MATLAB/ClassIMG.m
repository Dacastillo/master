classdef ClassIMG < handle
    properties
        h
        s
    end
    methods
        function start (obj) %Ejecución al iniciar el programa
            daq.reset; obj.s = daq.createSession('ni'); %Reiniciar y abrir la tarjeta
            co0 = addAnalogOutputChannel(obj.s, 'LAB', 'ao0', 'Voltage'); %Canal de Output X
            co1 = addAnalogOutputChannel(obj.s, 'LAB', 'ao1', 'Voltage'); %Canal de Output Y
            cc0 = addCounterInputChannel(obj.s, 'LAB', 'ctr0', 'EdgeCount'); %Canal Contador            
        end     
        function Image(obj) %Ejecución al apretar boton Start
            global arc;
            X1_A = str2double(get(obj.h.xce,'string')); Y1_A =  str2double(get(obj.h.yce,'string'));
            DX_A = str2double(get(obj.h.dex,'string')); DY_A =  str2double(get(obj.h.dey,'string'));
            N_A1 = str2double(get(obj.h.dot,'string')); N_A = int64(N_A1);
            tpause1_A = str2double(get(obj.h.tef,'string')); tpause2_A = str2double(get(obj.h.tin,'string'));
            if or(or(((X1_A + DX_A*0.5)> 80), ((X1_A - DX_A*0.5)< 0)), or(((Y1_A + DY_A*0.5)> 80), ((Y1_A - DY_A*0.5)< 0))) return; end
            A_zeros = 0; a=ones(N_A); [data,triggerTime] = obj.s.inputSingleScan; arc= 1;
            resetCounters(obj.s); A_zeros = obj.s.inputSingleScan; a = a *A_zeros; ax=1:1:N_A; b=1:1:N_A;
            datax = linspace((X1_A/8)-(DX_A/16),(X1_A/8)+(DX_A/16),N_A)'; datay = linspace((Y1_A/8)-(DY_A/16),(Y1_A/8)+(DY_A/16),N_A)';
            for i = 1:N_A
                for j = 1:N_A
                    outputSingleScan(obj.s,[datax(i) datay(j)]); pause(tpause1_A/1000); input(i,j,N_A,a,b, tpause2_A); stop(obj.s)
                    if(arc==0) break; end
                    drawnow();
                end
                if(arc==0) break; end
            end
            function input(x,y,Num,vec1,vec2, tpause2_A)
                if tpause2_A <= 25 tpause2_A=25; end
                cnt=0; A=0; obj.s.inputSingleScan; 
                for k = 1:round(tpause2_A/25) resetCounters(obj.s); cont1 = obj.s.inputSingleScan; A=A+cont1; end
                cnt=A; vec1(x,y)= cnt; vec2(y)= cnt; h = pcolor(obj.h.axes10,8*datax,8*datax,vec1); set(h, 'EdgeColor', 'none');
                colorbar(obj.h.axes10)
                colormap(obj.h.axes10,'jet')
                datacursormode on
                plot(obj.h.axes11,8*datax,vec2)
                a=vec1; b=vec2; set(obj.h.cux,'String',num2str(8*datax(x))); set(obj.h.cuy,'String',num2str(8*datay(y))); set(obj.h.cnt,'String', cnt);
            end
        end       
        function Trace(obj)
            global arct; tpause2_A = str2double(get(obj.h.tin,'string')); cnt=0; arct=1; Trace_lenght = 125; cnt=1:Trace_lenght; ene=0; alltrace = 0; row = 0;
            if tpause2_A <= 25 tpause2_A=25; end 
            while arct==1
                row = row+1; ene=ene+1; A=0; obj.s.inputSingleScan;
                for k = 1:round(tpause2_A/25)
                    resetCounters(obj.s); cont1 = obj.s.inputSingleScan; A=A+cont1;
                end
                cnt(ene)=A; alltrace = [alltrace cnt(ene)];
                if ene == Trace_lenght ene = 0; end
                if row >= Trace_lenght
                   cntaverage = mean(cnt); cntstd = std(cnt); set(obj.h.meancounts,'string',cntaverage); set(obj.h.stdcounts,'string',cntstd);
                end
                plot(obj.h.axes12,cnt(1:Trace_lenght))
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