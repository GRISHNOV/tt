do
    default_cfg = {
        pid_file  = "/var/run/tarantool",
        wal_dir   = "/var/lib/tarantool",
        memtx_dir = "/var/lib/tarantool",
        vinyl_dir = "/var/lib/tarantool",
        log       = "/var/log/tarantool",
        username  = "tarantool",
        language  = "Lua",
    }
    instance_dir = "/etc/tarantool/instances.enabled"
-- end