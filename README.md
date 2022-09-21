# CFX_Flood_Paint
Select the paint map you want to smooth and floood it!
<br>
<br>
**Author:** Bence Somosi
<br>
Script is only tested in Maya 2019.
<br>
<br>
Reach me here for more information or if you have any issues! https://www.linkedin.com/in/bensomosi/
<br>
<br>
## Documentation
Quick brief about how to install and use the tool.
<br>
<br>
### Install
Download the repository folder from my Github page.
<br><br>
Copy and paste the ```CFX_FloodPaint``` folder into your Maya folder.
<br>
The path should look like this: ```C:\Users\YOUR_USERNAME\Documents\maya\scripts```
<br>
<br>
After the installation you can run the script with these lines:
<br>
```python
from CFX_FloodPaint import CFX_FloodPaint_run
reload(CFX_FloodPaint_run)

windowFloodPaint = CFX_FloodPaint_run.FlooodPaintMainWindow()
windowFloodPaint.run()
```
### How to use it?
Quick brief about how the tool works.
<br>
<br>
![image](https://user-images.githubusercontent.com/19190277/191599999-4ac7db5f-7fd8-4c15-a3e0-c69e62ef5d45.png)
<br>
##### Amount of flooding
You can set here how many times you want to flood the paint map.
<br>
##### Floood it!
Press the the button to run the smooth iterations!
<br>
<br>
### Important notes
Before you start the flood process always make sure, you are in the Smooth paint mode.
<br>
<br>
![image](https://user-images.githubusercontent.com/19190277/191601123-f31310ca-e005-4ae9-97fc-894219092fbc.png)
<br>

