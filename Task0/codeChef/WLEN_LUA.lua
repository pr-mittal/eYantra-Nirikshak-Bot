--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code WLEN_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            WLEN_LUA.lua
*  Created:             07/10/2020
*  Last Modified:       07/10/2020
*  Author:              e-Yantra Team
*
*****************************************************************************************
]]--
 
-- countChar function to count the characters in each word of given string
function countChar(str)
    -- write your code here
    --[[str="@Debugging is being the detective in a criminal movie 
    where you are also the murderer"]]
    lTable={}
    for token in string.gmatch(str,"[^@%s]+")
    do
        table.insert(lTable,#token)
    end
    print(table.concat(lTable,","))
end
 
-- for each case, call countChar function to count the characters in each word of given string
tc = tonumber(io.read())
for i=1,tc
do
    str=io.read();
    countChar(str)
end
 
