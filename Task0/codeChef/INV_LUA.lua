--[[
***********
*
*
*  This script is code stub for CodeChef problem code INV_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            INV_LUA.lua
*  Created:             07/10/2020
*  Last Modified:       07/10/2020
*  Author:              e-Yantra Team
*
***********

1
3
Servo 3
Drone 6
Board 7
3
ADD LEDs 4
DELETE Board 4
DELETE Servo 4


ADDED Item LEDs
DELETED Item Board
Item Servo could not be DELETED
16



]]--
 
-- manageInventory function to add, update / delete items to / from the Inventory
function manageInventory()
    -- reading total Items N
    N = tonumber(io.read())
 
    local item_table= {}
    -- write your code here
    for i=1, N, 1  do
      Str=io.read()
      a=1
        item_table[i]={}
      for str in string.gmatch(Str, "[^%s]+") do
        item_table[i][a] = str
        -- io.write(scorelist[i][a])
        -- io.write(a)
        a=a+1
      end
    end
    
    -- for j=1, #item_table,1 do
    --   io.write(item_table[j][1]," ",item_table[j][2],"\n")
    -- end

    -- reading total M operations to perform
    M = tonumber(io.read())
    --print(M)
    -- a=a+1
    -- io.write(a,"a\n")
    -- write your code here
    for i=1, M, 1 do
        --print(i)
      command = {}
      x = io.read()
      k=1
      for str in string.gmatch(x, "[^%s]+") do
        command[k] = str
        -- io.write(scorelist[i][a])
        -- io.write(a)
        k=k+1
      end
      
      if(command[1]=="ADD") then
        --print("ADD")
        flag = true
        for j = 1, #item_table,1 do
          if(command[2]==item_table[j][1]) then
            if(tonumber(item_table[j][2])~=0) then
                --print(item_table[j][2])
                --print(item_table[j][2]~=0)
                -- io.write(item_table[j][1]," ",item_table[j][2],"\n")
                io.write("UPDATED Item "..command[2].."\n")
                temp=tonumber(item_table[j][2])
                temp = temp + tonumber(command[3])
                item_table[j][2]=tostring(temp)
                flag = false    
            end
            break
          end
        end
        if(flag) then
          io.write("ADDED Item "..command[2].."\n")
          item_table[N+1]={}
          item_table[N+1][1]=command[2]
          item_table[N+1][2]=command[3]
          N=N+1
        end
      else -- DELETE
        --print("DELETE")
        for j=1, #item_table,1 do
          if(command[2]==item_table[j][1]) then
            if(tonumber(item_table[j][2])~=0) then
                if(tonumber(command[3])>tonumber(item_table[j][2]))then
                  io.write("Item "..command[2].." could not be DELETED".."\n")
                else
                  io.write("DELETED Item "..command[2].."\n")
                  temp=tonumber(item_table[j][2])
                  temp = temp - tonumber(command[3])
                  item_table[j][2]=tostring(temp)
                end    
                flag = false
            end
            break
            -- elseif(tonumber((command[3]))==tonumber(item_table[i][2])) 
            
            
          end
        end
        if(flag) then
          io.write(command[2].." does not exist".."\n")
        end
      end
    end
    -- calculate the sum of items
    local sum = 0
    for j=1, #item_table,1 do
      sum = sum + tonumber(item_table[j][2])
      -- io.write(item_table[j][1]," ",item_table[j][2],"\n")
    end
    -- write your code here    
 
    io.write(sum)
end
 
-- for each case, call the manageInventory function to add, update / delete items to / from the Inventory
tc = tonumber(io.read())
i = 0
while i < tc do
    manageInventory()
    i = i + 1
end
