function varargout = Image(varargin)
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Image_OpeningFcn, ...
                   'gui_OutputFcn',  @Image_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
function Image_OpeningFcn(hObject, eventdata, handles, varargin)
handles.output = hObject;
guidata(hObject, handles);
global IMG;
IMG = ClassIMG;
IMG.h = handles;
IMG.start
function varargout = Image_OutputFcn(hObject, eventdata, handles) 
varargout{1} = handles.output;
function start_Callback(hObject, eventdata, handles)
global IMG
IMG.Image
function stop_Callback(hObject, eventdata, handles)
global IMG
IMG.Stop
function startTrace_Callback(hObject, eventdata, handles)
global IMG
IMG.Trace
function stopTrace_Callback(hObject, eventdata, handles)
global IMG;
IMG.StopTrace
function dot_Callback(hObject, eventdata, handles)
global N;
N = handles.dot.Value;
guidata(hObject, handles);
function dot_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
    set(hObject,'Value','100');
end
function tef_Callback(hObject, eventdata, handles)
global tpause1;
tpause1 = handles.tef.Value/1000;
guidata(hObject, handles);
function tef_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
    set(hObject,'Value','100');
end
function xce_Callback(hObject, eventdata, handles)
global X1;
X1 =handles.xce.Value;
guidata(hObject, handles);
function xce_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
    set(hObject,'Value','40');
end
function yce_Callback(hObject, eventdata, handles)
global Y1;
Y1 =handles.yce.Value;
guidata(hObject, handles);
function yce_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
    set(hObject,'Value','40');
end
function dex_Callback(hObject, eventdata, handles)
global DX;
DX = handles.dex.Value;
guidata(hObject, handles);
function dex_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
    set(hObject,'Value','80');
end
function dey_Callback(hObject, eventdata, handles)
global DY;
DY = handles.dey.Value;
guidata(hObject, handles);
function dey_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
    set(hObject,'Value','80');
end
function tin_Callback(hObject, eventdata, handles)
global tpause2;
tpause2 = handles.tin.Value;
guidata(hObject, handles);
function tin_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
    set(hObject,'Value','0');
end
function cux_Callback(hObject, eventdata, handles)
function cux_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
function cuy_Callback(hObject, eventdata, handles)
function cuy_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
function cnt_Callback(hObject, eventdata, handles)
function cnt_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
function scn_Callback(hObject, eventdata, handles)
function scn_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
function stp_Callback(hObject, eventdata, handles)
function stp_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
function tco_Callback(hObject, eventdata, handles)
function tco_CreateFcn(hObject, eventdata, handles)
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


