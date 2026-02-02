#include "AnsiFontsPackage"

int main(){
    cout << color("hello", RED) << endl;
    cout << variant("hello", BOLD) << endl;
    cout << mix("hello", RED, CLEAR, UDLINE) << endl;

    return 0;
}