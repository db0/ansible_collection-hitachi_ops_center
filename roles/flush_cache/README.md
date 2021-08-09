# Db0 Hitachi OPS Center role: flush_cache

This role will flush all or just part of the cache created by the cached_uri role.

## Requirements 

None

## Expected variables

None

## Optional variables

These variables have predefined defaults but they can be overriden during role import.

* pattern (String): The file parrenn (glob-style) which to delete. If this is not specified, the whole cache will be flushed
* cache_dir (String): The directory in whbich the cache is stored in the execution host.

These are variables set in the role defaults. 

* cache_dir: The location in which to look for cache files
