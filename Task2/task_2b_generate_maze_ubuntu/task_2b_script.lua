--[[
*****************************************************************************************
*
*        		===============================================
*           		Nirikshak Bot (NB) Theme (eYRC 2020-21)
*        		===============================================
*
*  This Lua script is to implement Task 2B of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using ICT (NMEICT)
*
*****************************************************************************************
]]--


--[[
# Team ID:			2182
# Author List:		Aman Sharma,Pranav Mittal
# Filename:			task_2b
# Functions:        createWall, saveTexture, retrieveTexture, reapplyTexture, receiveData, generateHorizontalWalls, 
#                   generateVerticalWalls, deleteWalls, createMaze, sysCall_init, sysCall_beforeSimulation
#                   sysCall_afterSimulation, sysCall_cleanup,setWallLocation,deleteWall
# 					[ Comma separated list of functions in this file ]
# Global variables:	
#                    maze_array
# 					[ List of global variables defined in this file ]
]]--

--[[
##################### GLOBAL VARIABLES #######################
## You can add global variables in this section according   ##
## to your requirement.                                     ##
## DO NOT TAMPER WITH THE ALREADY DEFINED GLOBAL VARIABLES. ##
##############################################################
]]--

maze_array = {}
baseHandle = -1       --Do not change or delete this variable
textureID = -1        --Do not change or delete this variable
textureData = -1       --Do not change or delete this variable
--############################################################

--[[
##################### HELPER FUNCTIONS #######################
## You can add helper functions in this section according   ##
## to your requirement.                                     ##
## DO NOT MODIFY OR CHANGE THE ALREADY DEFINED HELPER       ##
## FUNCTIONS                                                ##
##############################################################
]]--
function setWallLocation(pos,ori,name,parent)
    --make a wall element based on the info sent as arguments 
    local wallObjectHandle=createWall()
    sim.setObjectOrientation(wallObjectHandle, -1,ori)
    sim.setObjectPosition(wallObjectHandle,-1,pos)
    --print(name)
    sim.setObjectName(wallObjectHandle,name)
    sim.setObjectParent(wallObjectHandle,parent,true)
end
function deleteWall(name)
    --delete the wall element of that name if it exists
    handle=sim.getObjectHandle(name)
    if(handle~=-1)
    then
        sim.removeObject(sim.getObjectHandle(name))
    end
end
--[[
**************************************************************
	Function Name : createWall()
    Purpose:
	---
	Creates a black-colored wall of dimensions 90cm x 10cm x 10cm

	Input Arguments:
	---
	None
	
	Returns:
	---
	wallObjectHandle : number
    
    returns the object handle of the created wall
	
	Example call:
	---
	wallObjectHandle = createWall()
**************************************************************	
]]--
function createWall()
    wallObjectHandle = sim.createPureShape(0, 26, {0.09, 0.01, 0.1}, 0, nil)
    sim.setShapeColor(wallObjectHandle, nil, sim.colorcomponent_ambient_diffuse, {0, 0, 0})
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_collidable)
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_measurable)
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_detectable_all)
    sim.setObjectSpecialProperty(wallObjectHandle, sim.objectspecialproperty_renderable)
    return wallObjectHandle
end

--[[
**************************************************************
  YOU ARE NOT ALLOWED TO MODIFY OR CALL THIS HELPER FUNCTION
**************************************************************
	Function Name : saveTexture()
    Purpose:
	---
	Reads and initializes the applied texture to Base object
    and saves it to a file.

	Input Arguments:
	---
	None
	
	Returns:
	---
	None
	
	Example call:
	---
	saveTexture()
**************************************************************	
]]--
function saveTexture()
    baseHandle = sim.getObjectHandle("Base")
    textureID = sim.getShapeTextureId(baseHandle)
    textureData=sim.readTexture(textureID ,0,0,0,0,0)
    sim.saveImage(textureData, {512,512}, 0, "models/other/base_template.png", -1)
end
--[[
**************************************************************
  YOU ARE NOT ALLOWED TO MODIFY OR CALL THIS HELPER FUNCTION
**************************************************************
	Function Name : retrieveTexture()
    Purpose:
	---
	Loads texture from file.

	Input Arguments:
	---
	None
	
	Returns:
	---
	None
	
	Example call:
	---
	retrieveTexture()
**************************************************************	
]]--
function retrieveTexture()
    textureData, resolution = sim.loadImage(0, "models/other/base_template.png") 
end

--[[
**************************************************************
  YOU ARE NOT ALLOWED TO MODIFY OR CALL THIS HELPER FUNCTION
**************************************************************
	Function Name : reapplyTexture()
    Purpose:
	---
	Re-applies texture to Base object

	Input Arguments:
	---
	None
	
	Returns:
	---
	None
	
	Example call:
	---
    reapplyTexture()
**************************************************************	
]]--
function reapplyTexture()
    plane, textureID = sim.createTexture("", 0, nil, {1.01, 1.01}, nil, 0, {512, 512})
    sim.writeTexture(textureID, 0, textureData, 0, 0, 0, 0, 0)
    sim.setShapeTexture(baseHandle, textureID, sim.texturemap_plane, 0, {1.01, 1.01},nil,nil)
    sim.removeObject(plane)
end

--############################################################

--[[
**************************************************************
	Function Name : receiveData()
    Purpose:
	---
	Receives data via Remote API. This function is called by 
    simx.callScriptFunction() in the python code (task_2b.py)

	Input Arguments:
	---
	inInts : Table of Ints
    inFloats : Table of Floats
    inStrings : Table of Strings
    inBuffer : string
	
	Returns:
	---
	inInts : Table of Ints
    inFloats : Table of Floats
    inStrings : Table of Strings
    inBuffer : string
    
    These 4 variables represent the data being passed from remote
    API client(python) to the CoppeliaSim scene
	
	Example call:
	---
	N/A
    
    Hint:
    ---
    You might want to study this link to understand simx.callScriptFunction()
    better 
    https://www.coppeliarobotics.com/helpFiles/en/remoteApiExtension.htm
**************************************************************	
]]--
function receiveData(inInts,inFloats,inStrings,inBuffer)
    --print("Receive data called")
    --*******************************************************
    --               ADD YOUR CODE HERE
    --make 2D array from received 1D array
    --print(inInts)
    --print(maze_array)
    maze_array={}
    if(inInts==nil)
    then
        return
    end
    wall=10
    for i=1,#inInts,wall
    do
        local sub_list={}
        for j=i,wall+i-1,1
        do
            table.insert(sub_list,inInts[j])
        end
        table.insert(maze_array,sub_list)
    end
    --print(maze_array)
    --maze_array=inInts
    --*******************************************************
    return inInts, inFloats, inStrings, inBuffer
end

--[[
**************************************************************
	Function Name : generateHorizontalWalls()
    Purpose:
	---
	Generates all the Horizontal Walls in the scene.

	Input Arguments:
	---
	None
	
	Returns:
	---
    None
	
	Example call:
	---
	generateHorizontalWalls()
**************************************************************	
]]--
function generateHorizontalWalls()

    --*******************************************************
    --               ADD YOUR CODE HERE
    --[[(x,y)==(row,col)==(i,j)==ixj
    1x1 1x2 1x3 1x4 ..... 1x10
    2x1 2x2 ................
    .
    .
    10x1 10x2 ........... 10x10
    11x1 11x2 ........... 11x10
    ]]--
    wall=10
    x_gap=0.1
    y_gap=0.1
    --pos={0.05-0.1*5,0.01*5,0.08}
    pos={x_gap/2-x_gap*wall/2,y_gap*wall/2,0.08}
    ori={0,0,0}
    
    parent=sim.getObjectHandle("Base")
    for i=1,wall+1,1
    do
        for j=1,wall,1
        do
            local name="H_WallSegment_"..i.."x"..j
            --print(pos)
            setWallLocation(pos,ori,name,parent)
            --print(pos)
            --adding 0.01 to x,going left to right 
            --pos[1]=pos[1]+0.1
            pos[1]=pos[1]+x_gap
        end
        --reseting values of x , going left to right
        --pos[1]=0.05-0.1*5
        pos[1]=x_gap/2-x_gap*wall/2
        --subtracting 0.01 to y , coming one level down
        --pos[2]=pos[2]-0.1
        pos[2]=pos[2]-y_gap
    end
        
    --*******************************************************
end

--[[
**************************************************************
	Function Name : generateVerticalWalls()
    Purpose:
	---
	Generates all the Vertical Walls in the scene.

	Input Arguments:
	---
	None
	
	Returns:
	---
    None
	
	Example call:
	---
	generateVerticalWalls()
**************************************************************	
]]--

function generateVerticalWalls()

    --*******************************************************
    --               ADD YOUR CODE HERE
    --[[(x,y)==(row,col)==(i,j)==ixj
    1x1 1x2 1x3 1x4 ..... 1x10 1x11
    2x1 2x2 ................   2x11
    .
    .
    10x1 10x2 ........... 10x10 10x11
    ]]--
    wall=10
    x_gap=0.1
    y_gap=0.1
    --pos={-0.1*5,-0.05+0.1*5,0.08}
    pos={-x_gap*wall/2,-y_gap/2+y_gap*wall/2,0.08}
    ori={0,0,math.pi/2}
    
    parent=sim.getObjectHandle("Base")
    for i=1,wall,1
    do
        for j=1,wall+1,1
        do
            local name="V_WallSegment_"..i.."x"..j
            --print(pos)
            setWallLocation(pos,ori,name,parent)
            --print(pos)
            --adding 0.01 to x,going left to right 
            --pos[1]=pos[1]+0.1
            pos[1]=pos[1]+x_gap
        end
        --reseting values of x , going left to right
        --pos[1]=-0.05-0.1*5
        pos[1]=-x_gap*wall/2
        --subtracting 0.01 to y , coming one level down
        --pos[2]=pos[2]-0.1
        pos[2]=pos[2]-y_gap
    end
        
    --*******************************************************
end

--[[
**************************************************************
	Function Name : deleteWalls()
    Purpose:
	---
	Deletes all the walls in the given scene

	Input Arguments:
	---
	None
	
	Returns:
	---
    None
	
	Example call:
	---
	deleteWalls()
**************************************************************	
]]--
function deleteWalls()

    --*******************************************************
    --               ADD YOUR CODE HERE
    --"V_WallSegment_"..i.."x"..j[1-10,1-11]
    --"H_WallSegment_"..i.."x"..j[1-11,1-10]
    --deleting vertical walls
    wall=10
    --deleting all wall except i==j
    --removing runtime error on objectHandle not found
    local savedState=sim.getInt32Parameter(sim.intparam_error_report_mode)
    sim.setInt32Parameter(sim.intparam_error_report_mode,0)
    
    for i=1,wall,1
    do
        for j=1,wall,1
        do
            if(i==j)
            then
                --deleting (i,i) where i==(1:10)
                name="V_WallSegment_"..i.."x"..j
                deleteWall(name)
                name="H_WallSegment_"..j.."x"..i
                deleteWall(name)
                break
            end
            --deleting the (i,j) where i,j==(1:10,1:10)
            name="V_WallSegment_"..i.."x"..j
            deleteWall(name)
            name="H_WallSegment_"..i.."x"..j
            deleteWall(name)
            --deleting the (i,j) where i,j==(1:10,1:10)
            name="V_WallSegment_"..j.."x"..i
            deleteWall(name)
            
            name="H_WallSegment_"..j.."x"..i
            deleteWall(name)
        end
    end
    --deleting the 11th row/col of wall
    for i=1,wall,1
    do
        name="V_WallSegment_"..i.."x11"
        deleteWall(name)
        name="H_WallSegment_11x"..i
        deleteWall(name)
    end
    --reseting runtime error on objectHandle not found
    sim.setInt32Parameter(sim.intparam_error_report_mode,savedState)
    --*******************************************************
end


--[[
**************************************************************
  YOU CAN DEFINE YOUR OWN INPUT AND OUTPUT PARAMETERS FOR THIS
                          FUNCTION
**************************************************************
	Function Name : createMaze()
    Purpose:
	---
	Creates the maze in the given scene by deleting specific 
    horizontal and vertical walls

	Input Arguments:
	---
	None
	
	Returns:
	---
    None
	
	Example call:
	---
	createMaze()
**************************************************************	
]]--
function createMaze()
    
    --*******************************************************
    --               ADD YOUR CODE HERE
    
    --Horizontal walls
--[[(x,y)==(row,col)==(i,j)==ixj
    1x1 1x2 1x3 1x4 ..... 1x10
    2x1 2x2 ................
    .
    .
    10x1 10x2 ........... 10x10
    11x1 11x2 ........... 11x10
    ]]--
    --Vertical walls
--[[(x,y)==(row,col)==(i,j)==ixj
    1x1 1x2 1x3 1x4 ..... 1x10 1x11
    2x1 2x2 ................   2x11
    .
    .
    10x1 10x2 ........... 10x10 10x11
    ]]--        
    --*******************************************************
    --[[mazearray={{11, 2, 6, 3, 2, 10, 10, 6, 3, 6},
              {3, 4, 13, 5, 5, 11, 10, 8, 12, 5},
              {5, 5, 3, 12, 5, 3, 10, 10, 6, 5},
              {5, 13, 5, 3, 12, 9, 6, 3, 12, 13},
              {5, 3, 12, 9, 10, 10, 12, 9, 10, 6},
              {5, 9, 10, 10, 6, 3, 6, 3, 6, 5},
              {1, 6, 3, 10, 12, 5, 9, 12, 5, 13},
              {5, 5, 5, 11, 10, 4, 3, 6, 5, 7},
              {5, 5, 9, 10, 6, 5, 5, 9, 12, 5},
              {13, 9, 10, 10, 8, 12, 9, 10, 10, 12}}
    ]]--
    --print(mazearray)
    if(maze_array==nil)
    then
        return
    end
    --west=1,north=2,east=4,south=8
    
    wall=10
    --checking value of mazearray for alternate cells,no wall are common
    --deleteing accordingly,as no repeated deletion of walls can be allowed
    
    for i=1,wall,1
    do
        for j=i%2+1,wall,2
        do
            roi=maze_array[i][j]
            west=roi%2
            roi=math.floor(roi/2)
            north=roi%2
            roi=math.floor(roi/2)
            east=roi%2
            roi=math.floor(roi/2)
            south=roi%2
            --circumsiding wall for ixj roi ith row,jth col
            --west=ixj, north=ixj,south=i+1xj,east=ixj+1
            if(west==0)
            then
                name="V_WallSegment_"..i.."x"..j
                sim.removeObject(sim.getObjectHandle(name))
            end
            if(north==0)
            then
                name="H_WallSegment_"..i.."x"..j
                sim.removeObject(sim.getObjectHandle(name))
            end
            if(east==0)
            then
                name="V_WallSegment_"..i.."x"..j+1
                sim.removeObject(sim.getObjectHandle(name))
            end
            if(south==0)
            then
                name="H_WallSegment_"..(i+1).."x"..j
                sim.removeObject(sim.getObjectHandle(name))
            end
        end
    end

end



--[[
**************************************************************
	Function Name : sysCall_init()
    Purpose:
	---
	Can be used for initialization of parameters
    
	Input Arguments:
	---
	None
	
	Returns:
	---
    None
	
	Example call:
	---
	N/A
**************************************************************	
]]--
function sysCall_init()
    if pcall(saveTexture) then -- Do not delete or modify this section
        print("Successfully saved texture")
    else
        print("Texture does not exist. Importing texture from file..")
        retrieveTexture()
        reapplyTexture()
    end     
end

--[[
**************************************************************
        YOU ARE NOT ALLOWED TO MODIFY THIS FUNCTION. 
**************************************************************
	Function Name : sysCall_beforeSimulation()
    Purpose:
	---
	This is executed before simulation starts
    
	Input Arguments:
	---
	None
	
	Returns:
	---
    None
	
	Example call:
	---
	N/A
**************************************************************	
]]--
function sysCall_beforeSimulation()
    --print("Simulation started")
    sim.setShapeTexture(baseHandle, -1, sim.texturemap_plane, 0, {1.01, 1.01},nil,nil) -- Do not delete or modify this line
    
    generateHorizontalWalls()
    generateVerticalWalls()
    createMaze()
    
end

--[[
**************************************************************
        YOU ARE NOT ALLOWED TO MODIFY THIS FUNCTION. 
**************************************************************
	Function Name : sysCall_afterSimulation()
    Purpose:
	---
	This is executed after simulation ends
    
	Input Arguments:
	---
	None
	
	Returns:
	---
    None
	
	Example call:
	---
	N/A
**************************************************************	
]]--
function sysCall_afterSimulation()
    -- is executed after a simulation ends
    deleteWalls()
    reapplyTexture() -- Do not delete or modify this line
end

function sysCall_cleanup()
    -- do some clean-up here
end

-- See the user manual or the available code snippets for additional callback functions and details
