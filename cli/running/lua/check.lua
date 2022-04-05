-- This is a script that check an application file for syntax errors.
-- The application file passes throught "TT_CLI_INSTANCE".

-- The script is delivered inside the "tt" binary and is launched
-- to execution via the `-e` flag when starting the application instance.
-- AFAIU, due to such method of launching, we can reach the limit of the
-- command line length ("ARG_MAX") and in this case we will have to create
-- a file with the appropriate code. But, in the real world this limit is
-- quite high (I looked at it on several machines - it equals 2097152)
-- and we can not create a workaround for this situation yet.
--
-- Several useful links:
-- https://porkmail.org/era/unix/arg-max.html
-- https://unix.stackexchange.com/a/120842

local os = require('os')

local function check()
    local instance_path = os.getenv('TT_CLI_INSTANCE')
    if instance_path == nil then
        print('Failed to get instance path from TT_CLI_INSTANCE env variable')
        os.exit(1)
    end

    local rv, err = loadfile(instance_path .. '.lua')
    if rv == nil then
        print(string.format("Syntax errors detected: '%s'", err))
        os.exit(0)
    end

    print(string.format("Syntax of file '%s' is OK", instance_path))
end

check()
