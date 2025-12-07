# Patterns

| Pattern          | Description                                                                                       |
| :--------------- | :------------------------------------------------------------------------------------------------ |
| `~A`             | All messages                                                                                      |
| `~b EXPR`        | Messages which contain `EXPR` in the message body                                                 |
| `=b STRING`      | IMAP: Like `~b` but searches for `STRING` on the server                                           |
| `~B EXPR`        | Messages which contain EXPRin the whole message                                                   |
| `=B STRING`      | IMAP: LIke `~B` but searches for `STRING` on the server                                           |
| `~c EXPR`        | Messages carbon-copied to `EXPR`                                                                  |
| `%c GROUP`       | Messages carbon-copied to any member of `GROUP`                                                   |
| `~C EXPR`        | Messages either to: or cc: `EXPR`                                                                 |
| `%C GROUP`       | Messages either to: or cc: to any member of `GROUP`                                               |
| `~d [MIN]-[MAX]` | Messages with `date-sent` in a Date range                                                         |
| `~D`             | Deleted messages                                                                                  |
| `~e EXPR`        | Messages which contains `EXPR` in the `Sender` field                                              |
| `%e GROUP`       | Messages which contain a member of `GROUP` in the `Sender` field                                  |
| `~E`             | Expired messages                                                                                  |
| `~F`             | Flagged messages                                                                                  |
| `~f EXPR`        | Messages originating from `EXPR`                                                                  |
| `%f GROUP`       | Messages originating from any member of `GROUP`                                                   |
| `~g`             | Cryptographically signed messages                                                                 |
| `~G`             | Cryptographically encrypted messages                                                              |
| `~h EXPR`        | Messages which contain EXPRin the message header                                                  |
| `=h STRING`      | IMAP: Like `~h` but searches for `STRING` on the server (must be of the form `header: substring`) |
| `~H EXPR`        | Messages with a spam attribute matching `EXPR`                                                    |
| `~i EXPR`        | Messages which match `EXPR` in the `Message-ID` field                                             |
| `~I QUERY`       | Use `$external_search_command` to find messages with `Message-ID`s matching `QUERY`               |
| `~k`             | Messages which contain PGP key material                                                           |
| `~L EXPR`        | Messages either originated or received by `EXPR`                                                  |
| `%L GROUP`       | Message either originated or received by any member of `GROUP`                                    |
| `~l`             | Messages addressed to a known mailing list                                                        |
| `~m [MIN]-[MAX]` | Messages with numbers in the range `MIN` to `MAX`                                                 |
| `~m <[MAX]`      | Messages with numbers less than `MAX`                                                             |
| `~m >[MIN]`      | Messages with numbers greater than `MIN`                                                          |
| `~m [M]`         | Just message number `M`                                                                           |
| `~m [MIN],[MAX]` | Messages with offsets (from selected message) in the range `MIN` to `MAX`                         |
| `~M EXPR`        | Messages which contain a mime Content-Type matching `EXPR`                                        |
| `~n [MIN]-[MAX]` | Messages with a score in the range `MIN` to `MAX`                                                 |
| `~N`             | New messages                                                                                      |
| `~O`             | Old messages                                                                                      |
| `~p`             | Messages addressed to you (consults `$from`, `alternates`, and local account/hostname)            |
| `~P`             | Messages from you (consults `$from`, `alternates`, and local account/hostname)                    |
| `~Q`             | Messages which have been replied to                                                               |
| `~r [MIN]-[MAX]` | Messages with `date-received` in a Date range                                                     |
| `~R`             | Read messages                                                                                     |
| `~s EXPR`        | Messages having `EXPR` in the `Subject` field                                                     |
| `~S`             | Superseded messages                                                                               |
| `~t EXPR`        | Messages addressed to `EXPR`                                                                      |
| `~T`             | Tagged messages                                                                                   |
| `~u`             | Messages addressed to a subscribed mailing list                                                   |
| `~U`             | Unread messages                                                                                   |
| `~v`             | Messages part of a collapsed thread                                                               |
| `~V`             | Cryptographically verified messages                                                               |
| `~w EXPR`        | Newsgroups matching `EXPR`                                                                        |
| `~x EXPR`        | Messages which contain `EXPR` in the `References` or `In-Reply-To` field                          |
| `~X [MIN]-[MAX]` | Messages with `MIN` to `MAX` attachments                                                          |
| `~y EXPR`        | Messages which contain `EXPR` in their keywords                                                   |
| `~Y EXPR`        | Messages whose tags match `EXPR`                                                                  |
| `~z [MIN]-[MAX]` | Messages with a size in the range `MIN` to `MAX`                                                  |
| `=/ STRING`      | GMail: Custom server-side search for `STRING`                                                     |
| `~=`             | Duplicated messages (see `$duplicate_threads`)                                                    |
| `~#`             | Broken threads (see `$strict_threads`)                                                            |
| `~$`             | Unreferenced messages (requires threaded view)                                                    |
| `~(PATTERN)`     | Messages in threads containing messages matching `PATTERN`                                        |
| `~<(PATTERN)`    | Messages whose immediate parent matches `PATTERN`                                                 |
| `~>(PATTERN)`    | Messages having an immediate child matching `PATTERN`                                             |

