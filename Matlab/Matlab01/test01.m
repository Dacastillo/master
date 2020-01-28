s = daq.createSession('ni');
addAnalogInputChannel(s,'LAB', 0, 'Voltage');
addCounterInputChannel(s,'LAB', 0, 'EdgeCount');
s.DurationInSeconds = 0.026;
[data, time] = s.startForeground()
plot(time, data);