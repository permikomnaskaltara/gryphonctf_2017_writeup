/**
 * Created for the GryphonCTF 2017 challenges
 * By Amos (LFlare) Ng <amosng1@gmail.com>
**/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int login() {
    // Declare login variables
    int access = 0xff;
    char password[16];

    // Get password
    puts("Warning: Permanently added 'backend.cia.gov,96.17.215.26' (ECDSA) to the list of known hosts.");
    printf("root@backend.cia.gov's password: ");
    
    // Add one more to fgets for null byte
    fgets(password, 17, stdin);

    return access;
}

int main() {
    // Disable output buffering
    setbuf(stdout, NULL);

    // Declare main variables
    char input[8];

    // Send canned greeting
    puts("The authenticity of host 'backend.cia.gov (96.17.215.26)' can't be established.");
    puts("ECDSA key fingerprint is SHA256:1loFo62WjwvamuIcfhqo4O2PNdltJgSJ7fB3GpKLm4o.");
    printf("Are you sure you want to continue connecting (yes/no)? ");

    // Add one more to fgets for null byte
    fgets(input, 9, stdin);

    // Log user in
    int access = login();

    // Check privileges
    if (access >= 0xff || access < 0) {
        puts("INVALID ACCOUNT ACCESS LEVEL!");
    } else if (access <= 0x20) {
        puts("SUCCESSFULLY LOGGED IN AS ADMIN!");
        system("/bin/sh");
    } else {
        puts("SUCCESSFULLY LOGGED IN AS USER!");
        puts("ERROR: YOU HAVE BEEN FIRED!");
        exit(1);
    }
}
