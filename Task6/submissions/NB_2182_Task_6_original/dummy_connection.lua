function sysCall_init()
    --[[
    Purpose:
    ---
    start remote api servers

    Input Arguments:
    ---
    None
    Returns:
    ---
    None
    Example call:
    ---
    called automatically when simulation is started
    ]]--
    -- do some initialization here
    simRemoteApi.start(1499)
    simRemoteApi.start(1498)
    simRemoteApi.start(1497)
    --simRemoteApi.start(1496)
    --simRemoteApi.start(1495)
end

function sysCall_actuation()
    -- put your actuation code here
end

function sysCall_sensing()
    -- put your sensing code here
end

function sysCall_cleanup()
    -- do some clean-up here
end

-- See the user manual or the available code snippets for additional callback functions and details
