local flag = {
    0x4a,0x50,0x57,0x4d,0x4c,0x58,0x50,0x42,0x52,0x7b,0x57,0x67,0x34,0x5f,0x61,0x6b,0x34,0x5f,0x65,0x4f,0x34,0x5f,0x4f,0x33,0x75,0x5f,0x73,0x67,0x59,0x5f,0x32,0x37,0x34,0x38,0x39,0x32,0x37,0x33,0x7d
}

local function encryptChar(char, shift)
    local byte = string.byte(char)
    if byte >= 65 and byte <= 90 then
        byte = ((byte - 65 + shift) % 26) + 65
    elseif byte >= 97 and byte <= 122 then
        byte = ((byte - 97 + shift) % 26) + 97
    end
    return string.char(byte)
end

local function check(input, idx)
    local enc = encryptChar(string.char(input), idx)
    if enc == string.char(flag[idx]) then
        return true
    else
        return false
    end
end

local function checkFlag(input)
    local inputBinary = {}

    for i = 1, #input do
        table.insert(inputBinary, string.byte(input:sub(i, i)))
    end

    if #inputBinary ~= #flag then
        print("Input length needs to be " .. #flag .. " characters!")
        return false
    end

     local checkResult = {}
    for i = 1, #inputBinary do
        table.insert(checkResult, check(inputBinary[i], i))
    end

    local count = 0
    for i, value in ipairs(checkResult) do
       count = count + (value and 1 or 0)
    end
    return count == #flag
end

io.write("Enter the flag: ")
local input = io.read()

if checkFlag(input) then
    print("Congratulations! You've found the correct flag.")
else
    print("Sorry, the flag is not correct. Try again.")
end
