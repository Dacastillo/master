daq.reset;
s = daq.createSession('ni');
addAnalogInputChannel(s,'LAB', 0, 'Voltage');
addCounterInputChannel(s,'LAB', 0, 'EdgeCount');
addAnalogOutputChannel(s, 'LAB', 'ao0', 'Voltage');
s.Rate = 10000; a = 0:0.01:0.5;
lh = addlistener(s,'DataAvailable', @plotData)
queueOutputData(s,a');
s.startBackground();
function plotData(src,event)
           NewData01 = event.Data(:,2);
           NewData02 = event.TimeStamps;
           NewData03 = NewData01(10:end)./NewData02(10:end);
           plot(event.TimeStamps,event.Data(:,2))
end