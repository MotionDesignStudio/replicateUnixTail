Description:

This replicates the tail functionality on Unices.  One of the functions does a system call to the tail command.  I tested it using a text file 1.8M in size.

These are the run times for each function using the same file.

def replicateUnixTail

real	0m0.036s
user	0m0.032s
sys	0m0.000s

def replicateUnixTail2

real	0m0.046s
user	0m0.040s
sys	0m0.004s

def replicateUnixTail3

real	0m0.034s
user	0m0.028s
sys	0m0.000s


Example usage:

#
replicateUnixTail (file_source="street.txt", start_from=10, increment_in_bytes=-256 )

#
replicateUnixTail2 (file_source="street.txt", start_from=10, increment_in_bytes=-256 )

#
replicateUnixTail3 (file_source="street.txt", startfrom=-10 )
