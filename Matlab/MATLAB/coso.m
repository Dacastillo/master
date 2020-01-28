clear, clc, close all; 
daq.reset; 
s = daq.createSession('ni');
s.Rate = 50000;
s.IsContinuous = true; 
n_channels = 4;
co1 = addAnalogOutputChannel(s, 'LAB', 'ao0', 'Voltage');
co2 = addAnalogOutputChannel(s, 'LAB', 'ao1', 'Voltage');
co3 = addAnalogOutputChannel(s, 'LAB', 'ao2', 'Voltage');
ci0 = addAnalogInputChannel(s, 'LAB', 'ai0', 'Voltage');
ci1 = addAnalogInputChannel(s, 'LAB', 'ai1', 'Voltage')
ci2 = addAnalogInputChannel(s, 'LAB', 'ai2', 'Voltage');
cc0 = addCounterInputChannel(s, 'LAB', 'ctr0', 'EdgeCount');
di0 = addDigitalChannel(obj.s, 'LAB', 'Port0/Line0:7', 'OutputOnly');
addClockConnection(obj.s,'External','LAB/PFI8','ScanClock');
ci1.TerminalConfig = 'SingleEnded';
ci2.TerminalConfig = 'SingleEnded';
ci3.TerminalConfig = 'SingleEnded';
cc0.ActiveEdge = 'Rising'
cc0.CountDirection = 'Increment'
cco.Terminal = 'PFI0'
for c = 0:3
s.UserData.Data = []; 
s.UserData.TimeStamps = [];
s.UserData.StartTime = [];
datax = sin(linspace(-15, 5, 50000)');
datay = sin(linspace(-10, 10, 50000)');
dataz = sin(linspace(-5, 15, 50000)');
queueOutputData(s,[datax,datay,dataz]);
lh1 = addlistener(s, 'DataAvailable', @recordData);
lh2 = addlistener(s, 'ErrorOccurred', @(~,eventData) disp(getReport(eventData.Error)));
startBackground(s);
while s.IsRunning
        pause(0.01);
end
pause(0.01);
stop(s)
delete(lh1); 
delete(lh2);
ai0 = s.UserData.Data(:,1); 
ai1 = s.UserData.Data(:,2); 
ai2 = s.UserData.Data(:,3); 
cc0 = s.UserData.Data(:,4);  
DAQ_2 = timetable(seconds(s.UserData.TimeStamps),ai0,ai1,ai2,cc0);
plot(DAQ_2.Time, DAQ_2.Variables); 
xlabel('Time'); 
ylabel('Amplitude (V)'); 
legend(DAQ_2.Properties.VariableNames);
end
clear lh1 lh2;
function recordData(src, eventData) 
src.UserData.Data = [src.UserData.Data; eventData.Data]; 
src.UserData.TimeStamps = [src.UserData.TimeStamps; 
eventData.TimeStamps];
if isempty(src.UserData.StartTime) 
    src.UserData.StartTime = eventData.TriggerTime;
end
end
 