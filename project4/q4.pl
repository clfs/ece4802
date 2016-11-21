#!/usr/bin/env perl6

use Digest::SHA;
use Path::Tiny;

my $pass_file = 'passwords.txt';
my $dict_File = 'dictionary.txt';

my @dict_content = Path::Tiny.path($dict_file).lines_utf8;
my @pass_content = Path::Tiny.path($pass_file).lines_utf8;

#print join('\n',@pass_content),'\n';

#my @hashdict = map {hash($_)} @dict_content;
#my @plaintexts = map {crack($_)} @pass_content;

#print join('\n',@plaintexts),'\n';
#print join('\n',@hashdict),'\n';

#### sub routines

#sub hash {
#    my ($message $rounds $salt) = parse(@_);
#    my $digest = sha512_hex($salt . $message);
#    $rounds--;
#    for (1..rounds)
#}
