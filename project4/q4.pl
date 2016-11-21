#!/usr/bin/perl

use strict;
use warnings;

use Digest::SHA qw(sha512_hex);
use Path::Tiny qw(path);

#### main routine ####

my $pass_file = shift or die "Usage: $0 PASSFILE DICTFILE";
my $dict_file = shift or die "Usage: $0 PASSFILE DICTFILE";

my @dict_content = path($dict_file)->lines_utf8;
my @pass_content = path($pass_file)->lines_utf8;

my @dict_hashes; # hash for line in dictionary file
my @pass_broken; # cracked passwords for line in password file

foreach my $d_line (@dict_content) {push @dict_hashes, hash($d_line);
foreach my $p_line (@pass_content) {push @pass_broken, crack($p_line);

print join('\n',@pass_broken),'\n';


# open files
#open my $pass_fh, '<', 'passwords.txt';
#open my $dict_fh, '<', 'dictionary.txt';
#
#my @dict_hashes;        # sha512 hashes for each line in dictionary.txt
#my @cracked_passes;     # cracked passwords for each line in passwords.txt
#
## hash dictionary.txt
#while (my $dict_line = <$dict_fh>) {
#    chomp $dict_line;
#    push @dict_hashes, sha512_hex($dict_line);
#}
#
# crack passwords.txt
#while (my $pass_line = <$pass_fh>) {
#    chomp $pass_line;
#    push @cracked_passes, crack($pass_line);
#}
#
#conditional_print(@cracked_passes)

#### sub routines ####

#sub crack {
#
#}

#sub parse {
#    $pass_line = @_;
#
#}

#sub 

#my @pass_fields;
#while (my $pass_line = <$pass_fh>) {
#    chomp $pass_line;
#    @pass_fields = parser($pass_line);
#    crack(@pass_fields);
#}

#my @pass_fields;
#my @pass_line;
#my @fields;
#
#while (my $line = <$pass_fh>) {
#    chomp $line;
#    @fields = split(/\$/, $line);
#   if (scalar @fields == 3) {splice @fields, 1, 0, '1';}
#    crack(@fields);
#}
#
#sub crack {
#    my ($id, $rounds, $salt, $data) = @_;
#    print "$id $rounds $salt $data\n";
#}
