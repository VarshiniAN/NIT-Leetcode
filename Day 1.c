#include<stdio.h>
#include<string.h>
#include<ctype.h>
int palindrome(char s[]) {
    int left = 0, right = strlen(s) - 1;
    while (left < right) {
        while (left < right && !isalnum((unsigned char)s[left])) left++;
        while (left < right && !isalnum((unsigned char)s[right])) right--;
        if (tolower((unsigned char)s[left]) != tolower((unsigned char)s[right])) {
            return 0;
        }
        left++;
        right--;
    }
    return 1;
}
int main() {
    char s[200];
    if (fgets(s, sizeof(s), stdin) != NULL) {
        s[strcspn(s, "\n")] = '\0';
    }
    if (palindrome(s)) {
        printf("Palindrome\n");
    }
    else {
        printf("Not Palindrome\n");
    }
    return 0;
}
