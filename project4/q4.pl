#!/usr/bin/perl

use strict;
use warnings;

use Digest::SHA qw(sha256_hex sha512_hex);
use Digest::MD5 qw(md5_hex);

open my $pass_fh, '<', 'passwords.txt';
open my $dict_fh, '<', 'dictionary.txt';

my @fields;

while ( my $line = <$pass_fh> ) {
    chomp $line;
    @fields = split(/\$/, $line);
    if (scalar @fields == 3) {splice @fields, 1, 0, '1';}
    crack(@fields);
}

sub crack {
    my ($id, $rounds, $salt, $data) = @_;
    print "$id $rounds $salt $data\n";
}
