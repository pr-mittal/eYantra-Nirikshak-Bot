# **eYRC 202021: Nirikshak Bot (NB)**

In this theme, teams will design **2-DOF Ball Balancing Platforms** capable of **navigating the balls through mazes** placed on top of the said platforms.

![2_arena_with_platform_tables](https://raw.githubusercontent.com/kalindkaria/typora-md-assets/master/maze_bot/assets/rb/2_arena_with_platform_tables.png)

- Platform Tables

  These are the Ball Balancing Platforms (designed by teams) 

- Conveyor Belt

  These are belts used to transfer balls

  | Belt Name            | Source of Ball     | Destination of Ball |
  | -------------------- | ------------------ | ------------------- |
  | Conveyor-Belt-1 (B1) | Table-4(T4)        | Table-1 (T1)        |
  | Conveyor-Belt-2 (B2) | Table-4(T4)        | Table-2 (T2)        |
  | Conveyor-Belt-3 (B3) | Table-4(T4)        | Table-3 (T3)        |
  | Conveyor-Belt-4 (B4) | Ball Dispenser(BD) | Table-4 (T4)        |

   

- Ball Dispenser

  A mechanism shown in Figure 3, will dispense the balls on to the **B4** at a **regular interval** of **80 simulation seconds**.

  The first ball will be dispensed at time **t = 0 sec**.

- Few Collection Boxes

  For each of the **three** Platform Tables (**T1**, **T2** and **T3**), there can be a **minimum of one** and **maximum of three** Collection Boxes associated in which the balls are to be dropped finally.

  | Platform Table Name | Collection Box 1 Name | Collection Box 2 Name | Collection Box 3 Name |
  | ------------------- | --------------------- | --------------------- | --------------------- |
  | Table-1 (**T1**)    | **T1_CB1**            | **T1_CB2**            | **T1_CB3**            |
  | Table-2 (**T2**)    | **T2_CB1**            | **T2_CB2**            | **T2_CB3**            |
  | Table-3 (**T3**)    | **T3_CB1**            | **T3_CB2**            | **T3_CB3**            |

- Vision Sensor

  There are **five** Vision Sensors in the Arena, out of which **four** are placed directly above the **four** Platform Tables coinciding with their center and looking downwards onto the Tables.

  The **fifth** Vision Sensor is placed above the Conveyor-Belt-1 (**B1**).

  

![5_arena_side_view_vision_sensors](https://raw.githubusercontent.com/kalindkaria/typora-md-assets/master/maze_bot/assets/rb/5_arena_side_view_vision_sensors.png)

#### Theme Run Requirements

Teams will be provided with the following files before the start of theme run:

1. **`arena_scene.ttt`** - This is the CoppeliaSim scene file in which the theme run will take place.

2. **`arena_scene_details.pdf`** - This document will define the objects / elements of **`arena_scene.ttt`**, their position, dimensions and properties.

3. **`ball_details.json`** - This JSON file provides the details of all balls that will be dispensed by the **BD**. The **color** and the **drop location** (i.e. a particular Collection Box) of each ball will be specified.

4. `maze_t1.jpg`

   , 

   `maze_t2.jpg`

   , 

   `maze_t3.jpg`

    and 

   `maze_t4.jpg`

    \- These are the image files of the mazes to be generated on top of the  four Platform Tables. These files are named according to the Platform  Table on which that particular maze is to be generated.

   - **`maze_t1.jpg`** - to be generated on **T1**
   - **`maze_t2.jpg`** - to be generated on **T2**
   - **`maze_t3.jpg`** - to be generated on **T3**
   - **`maze_t4.jpg`** - to be generated on **T4**

#### JSON File Description

```python
{
    "red"	: ["T1_CB3", "T2_CB1"],
    "green"	: ["T3_CB2"],
    "blue"	: ["T1_CB1", "T3_CB1"]
}
```

The above dictionary conveys the following information:

**Total number of balls to be dispensed by BD:** There are in total five balls that will be dispensed by the BD.
**Color of each ball:** There will be two red, one green and two blue balls dispensed by the BD in random order.
**Drop location of each ball:** The drop location i.e., the name of Collection Box in which balls are to be dropped, is given as list of strings corresponding to the color of each ball.

> **NOTE:**
>
> - The balls will be dispensed by the **BD** in ***random order***.
> - This means that at the very beginning, the first ball dispensed by the **BD** may or may not be **red** in color.
> - Similarly, at the very end, the last ball dispensed by the **BD** may or may not be **blue** in color.

#### Goal

There will be pre-defined number of balls and their drop locations that will be dispensed by the **BD** at **regular interval** of **80 simulation seconds**, which can be determined from the **`ball_details.json`** file provided before the theme run.

- Before the theme run starts, teams will import their **Ball Balance Platform** design in **`arena_scene.ttt`** file. The coordinates to which these platforms are to be positioned will be defined in **`arena_scene_details.pdf`**.
- Teams will start their Python client script, process the four maze  image files provided using Image Processing and generate these mazes on  top of the **four** Platform Tables in the **`arena_scene.ttt`**. The maze generation takes place with the help of customisation Lua script(s) in CoppeliaSim.
- Once the simulation starts, the Ball Dispenser (**BD**) will start dispensing each ball at regular interval of **80 simulation seconds**.
- The **Theme Run Timer** will start **as soon as the first ball** is transferred on to Table-4 (**T4**) by Conveyor-Belt-4 (**B4**).
- **T4** has to navigate the ball through maze on it and pass the ball to the next table i.e., **T1** or **T2** or **T3** based on the designated drop location mentioned in **`ball_details.json`** file.
- The next table will then navigate the ball through maze on it and drop the ball in the appropriate Collection Box (**CB**).
- The second ball will be dispensed at **80 simulation seconds** after the first ball was dispensed. This will repeat itself until the last ball is dispensed.
- The **Theme Run Timer** will **end after 480 simulation seconds** from the start of timer.
- The objective is to drop all the balls to their respective **CB** within **480 simulation seconds**.

## Arena

- Each team will be provided with a set of **four** maze image files (**`maze_t1.jpg`** to **`maze_t4.jpg`**) for the mazes to be generated on the four Platform Tables.
- The image for **T4** will have a maze of **10 x 10** net traversable cells.
- The images for **T3**, **T2** and **T1** will have a maze of **8 x 8** net traversable cells.

the **resultant maze** on **T4** should resemble 

![10_resultant_maze_on_T4](https://raw.githubusercontent.com/kalindkaria/typora-md-assets/master/maze_bot/assets/rb/10_resultant_maze_on_T4.png)

| T1     | <img src="https://raw.githubusercontent.com/kalindkaria/typora-md-assets/master/maze_bot/assets/rb/12a_resultant_maze_on_T1.png" alt="12a_resultant_maze_on_T1" style="zoom: 50%;" /> |
| ------ | ------------------------------------------------------------ |
| **T2** | <img src="https://raw.githubusercontent.com/kalindkaria/typora-md-assets/master/maze_bot/assets/rb/12b_resultant_maze_on_T2.png" alt="12b_resultant_maze_on_T2" style="zoom:50%;" /> |
| **T3** | <img src="https://raw.githubusercontent.com/kalindkaria/typora-md-assets/master/maze_bot/assets/rb/12c_resultant_maze_on_T3.png" alt="12c_resultant_maze_on_T3" style="zoom:50%;" /> |

The **ENTRY** and **EXIT** cells for **T1**, **T2**, **T3** and **T4** will remain same irrespective of the maze images.

## Theme Rules

- The **maximum time** allotted to complete the task is **480 simulation seconds**.
- A **maximum of two runs** will be given to each team from which the **best of the two runs** will be counted as the **final score**.
- A **maximum of one restart** is allowed per run wherein the Python client script, the CoppeliaSim simulation and the Theme Run  timer will start again. In case a team requires a *second restart*, the **run will be ended** and **maximum time** for the task (**480 simulation seconds**) will be considered for that run.
- If during simulation, any kind of collision or balancing of Platform Tables causes any **changes in the arena configuration**, then it will result in **immediate end** of the run and **maximum time** for the task (**480 simulation seconds**) will be considered for that run.
- Teams will be provided with the following files before the start of theme run:
  - **`arena_scene.ttt`**
  - **`arena_scene_details.pdf`**
  - **`ball_details.json`**
  - **`maze_t1.jpg`**, **`maze_t2.jpg`**, **`maze_t3.jpg`** and **`maze_t4.jpg`**
- Teams will import their **Ball Balance Platform** design in **`arena_scene.ttt`** file. The coordinates to which these platforms are to be positioned will be defined in **`arena_scene_details.pdf`**.
- Teams will start their Python client script, process the four maze  image files provided using Image Processing and generate these mazes on  top of the **four** Platform Tables in the **`arena_scene.ttt`**. The maze generation takes place with the help of customisation Lua script(s) in CoppeliaSim.
- Once the simulation starts, the Ball Dispenser (**BD**) will start dispensing each ball at regular interval of **80 simulation seconds**.
- The **Theme Run Timer** will start **as soon as the first ball** is transferred on to Table-4 (**T4**) by Conveyor-Belt-4 (**B4**).
- Teams have to make **T4** navigate the ball through maze on it and pass the ball to the next table i.e., **T1** or **T2** or **T3** based on the designated drop location mentioned in **`ball_details.json`** file.
- The next table will then navigate the ball through maze on it and drop the ball in the appropriate Collection Box (**CB**).
- The **second ball** will be dispensed at **80 simulation seconds** after the first ball was dispensed.
- This process will repeat itself until the last ball is dispensed.
- The **Theme Run Timer** will **end after 480 simulation seconds** from the start of timer.
- The objective is to drop all the balls to their respective **CB** within **480 simulation seconds**.
- Each **Platform Table** that is able to **pass / drop each ball to the next table / the designated CB within the stipulated amount of time** is considered as ***OK Tested!***



- A run ends and the 

  Theme Run Timer

   is stopped when:

  - If the maximum time limit of **480 simulation seconds** for completing the task is reached **OR**
  - If the team needs a second restart but has already used first restart for that run **OR**
  - If any of the Platform Tables or any kind of collision while performing the task causes any **changes in the arena configuration**.

- Second run will start after the first whilst resetting the score, timer and the arena.

- The score of both runs will be recorded and best of two runs will be considered as the team's final score.

  > May the *PID* be with you! 😛