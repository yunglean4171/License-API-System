local id = GetCurrentServerEndpoint() --in this case id = server ip
local licensekey = Config.licensekey

function Verificate()
    local ResourceName = GetCurrentResourceName()

    PerformHttpRequest('http://127.0.0.1:5000/' .. licensekey .. '/' .. id, function(statusCode, resultData, resultHeaders)

        if statusCode == 200 then
            local data = json.decode(resultData)
            if data == "true" then
                print('^5 [' .. ResourceName .. '] - ^7Auth Validated')
                TriggerClientEvent('StartClientCode', -1)
                Main()
            else
                print('^1 [' .. ResourceName .. '] - ^7Auth Not Validated')
            end
            
    end, 'GET')
end

function Main()
    -- Add your code here
end

AddEventHandler('onResourceStart', function(resourceName)
    if (GetCurrentResourceName() == resourceName) then
        Verificate()
    end
end)