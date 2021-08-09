# Db0 Hitachi OPS Center role: cached_uri

This role will retrieve and cache a REST API result from the specified URI, using the ansible uri module, then store it in a predefined location. If the specified URI has already been cached and within its TTL, it will use the cached version.

Finally, the content of the cached or fresh URI call, will be set inside the specified variable name.

## Requirements 

None

## Expected variables

These variables must be passed to the role during import.

* full_uri (String): The complete URI from which to retrieve the content
* uri_auth_token (String): The authentication token to use to connect to HOPSC
* register_name (String): The variable name in which to return the content of the uri call.

## Optional variables

These variables have predefined defaults but they can be overriden during role import.

* timeout (int): The amount of seconds to wait for the API to respond.
* uri_remote_auth_token (String): In case the API call requires authentication on two arrays, you pass the remote array's auth token as this variable. If this is not passed, this header will be skipped.

These are variables set in `defaults/main.yml`.

* cache_dir: The location in which to store/retrieve the cache in the execution host
* cache_ttl: The time-to-live in seconds for the cache. 
