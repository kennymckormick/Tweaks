#!/usr/bin/expect
trap {
    set rows [stty rows]
    set cols [stty columns]
    stty rows $rows columns $cols < $spawn_out(slave,name)
} WINCH
eval spawn ssh username@server
expect "*Verification code:*"
send [exec cat dyn_code.txt]
send "\r"
expect "Password:"
send [exec cat password.txt]
send "\r"
interact
