#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char **argv) {
    if(argc<=1)
        return 0;
    int rc = fork();
    argv[argc-1] = NULL;
    --argc;
    if(rc<0)
        return -1;
    else if (0==rc)
        main(argc,argv);
    else
        execvp(argv[0],argv);
    return 0;
}
