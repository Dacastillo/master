function guitrial
S.voltageH = uicontrol('Style', 'PushButton',...
    'String', 'Voltage', ...
    'Position', [10, 200, 100, 24], ...
    'Callback', {@dataaq});
S.ValueH = uicontrol('Style', 'edit', 'String', '0', ...
    'Position', [10, 150, 100, 24]);
guidata(gcf,S)
    function [] = dataaq(varargin)
        D = randi(10);  % Say your program returns this.
        S = guidata(gcbf);
        set(S.ValueH,'string',num2str(D));
    end
end