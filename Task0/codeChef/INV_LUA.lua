--[[
*****************************************************************************************
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
*****************************************************************************************
]]--
 
-- manageInventory function to add, update / delete items to / from the Inventory
function manageInventory()
    -- reading total Items N
    N = tonumber(io.read())
 
    -- write your code here
    inv={}
    for i=1,N,1
    do
      for key,value in string.gmatch(io.read(),"(%w+)%s+(%w+)")
      do 
        -- print(#key)
        -- print(#value)
        inv[key]=tonumber(value)
      end
    end
 
    -- reading total M operations to perform
    M = tonumber(io.read())
 
    -- write your code here
    for i=1,M,1
    do
      for op,indx,qty in string.gmatch(io.read(),"(%w+)%s+(%w+)%s+(%w+)")
      do 

        qty=tonumber(qty)
        -- print(#op,op)
        -- print(#indx,indx)
        -- print(#qty,qty)
        if(op=="ADD")
        then
          -- print("ADD")
          if(inv[indx]==nil)
          then
            inv[indx]=qty
            -- print ADDED Item item_name
            io.write("ADDED Item "..indx.."\n")
          else
            inv[indx]=inv[indx]+qty
            io.write("UPDATED Item "..indx.."\n")
          end
          -- print(inv[indx])
        elseif(op=="DELETE")
        then
          -- print("DELETE")
          if(inv[indx]==nil)
          then
            io.write("Item "..indx.." does not exist\n")
          else
            if(inv[indx]<qty)
            then
              io.write("Item "..indx.." could not be DELETED\n")
            else
              inv[indx]=inv[indx]-qty
              io.write("DELETED Item "..indx.."\n")
            end
          end
        end
    
    
      end
    end
 
    -- calculate the sum of items
    local sum = 0
 
    -- write your code here    
    for key,value in pairs(inv)
    do
      sum=sum+value
    end
    print(sum)
end
 
-- for each case, call the manageInventory function to add, update / delete items to / from the Inventory
tc = tonumber(io.read())
i = 0
while i < tc do
    manageInventory()
    i = i + 1
end
 
