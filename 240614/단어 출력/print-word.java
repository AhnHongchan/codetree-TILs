// 클래스 선언:
// 자바 프로그램은 클래스 단위로 작성됩니다. 클래스 이름은 파일 이름과 같아야 하며, 대문자로 시작하는 것이 관례입니다.
public class Main {
    // 메인 메소드:
    // 자바 프로그램의 시작점입니다. 모든 자바 애플리케이션에는 public static void main(String[] args) 메소드가 하나 있어야 합니다.

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        // 출력
        System.out.print("Hello");
    }
}

/*

public class Main:

public은 접근 제어자로, 이 클래스가 다른 클래스에서 접근 가능함을 의미합니다.
class 키워드는 클래스를 정의할 때 사용됩니다.
Main은 클래스의 이름입니다.

public static void main(String[] args):

public은 메소드가 다른 클래스에서 호출될 수 있음을 의미합니다.
static은 이 메소드가 클래스의 인스턴스 없이 호출될 수 있음을 의미합니다.
void는 이 메소드가 값을 반환하지 않음을 의미합니다.
main은 메소드의 이름입니다. 자바 프로그램의 진입점으로 사용됩니다.
String[] args는 명령줄 인수를 저장하는 배열입니다.

System.out.print("Hello");:

System.out은 자바의 표준 출력 스트림을 나타냅니다.
print 메소드는 괄호 안의 문자열을 콘솔에 출력합니다.
요약
자바 프로그램은 클래스와 메소드로 구성되며, 프로그램의 진입점인 main 메소드가 있어야 합니다. System.out.print와 같은 출력문을 사용하여 콘솔에 텍스트를 출력할 수 있습니다. 위의 예제는 "Hello"를 콘솔에 출력하는 간단한 자바 프로그램입니다.
*/