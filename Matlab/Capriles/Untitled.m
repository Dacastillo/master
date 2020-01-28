
import java.awt.Robot;
import java.awt.event.*;
mouse = Robot;
for i=1:10
mouse.mousePress(InputEvent.BUTTON1_MASK);
mouse.mouseRelease(InputEvent.BUTTON1_MASK);
pause(1)
end
