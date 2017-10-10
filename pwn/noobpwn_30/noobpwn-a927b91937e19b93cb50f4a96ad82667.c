/**
 * Created for the GryphonCTF 2017 challenges
 * By Amos (LFlare) Ng <amosng1@gmail.com>
**/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc){
    // Create buffer
    char buf[32] = {0x00};
    int key = 0x00;

    // Disable output buffering
    setbuf(stdout, NULL);

    // Get key?
    printf("Key? ");
    scanf("%d", &key);

    // Create file descriptor
    int fd = key - 0x31337;
    int len = read(fd, buf, 32);

    // Check if we have a winner
    if (!strcmp("GIMMEDAFLAG\n", buf)) {
        system("/bin/cat flag.txt");
        exit(0);
    }

    // Return sadface
    return 1;
}
