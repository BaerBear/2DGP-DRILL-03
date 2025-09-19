from pico2d import *
import math

open_canvas()

# 캐릭터 이미지 로드
character = load_image('character.png')

def draw_character(x, y):
    """캐릭터를 화면에 그리기"""
    clear_canvas_now()
    character.draw_now(x, y)
    delay(0.01)

def move_rectangle():
    """사각형 운동"""
    print("사각형 운동 시작")

    # 위쪽 변 (좌 → 우)
    for x in range(100, 700, 5):
        draw_character(x, 500)

    # 오른쪽 변 (위 → 아래)
    for y in range(500, 200, -5):
        draw_character(700, y)

    # 아래쪽 변 (우 → 좌)
    for x in range(700, 100, -5):
        draw_character(x, 200)

    # 왼쪽 변 (아래 → 위)
    for y in range(200, 500, 5):
        draw_character(100, y)

def move_triangle():
    """삼각형 운동"""
    print("삼각형 운동 시작")

    # 첫 번째 변: 좌하 → 우하
    for x in range(200, 600, 5):
        draw_character(x, 200)

    # 두 번째 변: 우하 → 중상 (대각선)
    steps = 80
    for i in range(steps):
        x = 600 - (200 * i // steps)
        y = 200 + (200 * i // steps)
        draw_character(x, y)

    # 세 번째 변: 중상 → 좌하 (대각선)
    for i in range(steps):
        x = 400 - (200 * i // steps)
        y = 400 - (200 * i // steps)
        draw_character(x, y)

def move_circle():
    """원형 운동"""
    print("원형 운동 시작")
    center_x, center_y = 400, 300
    radius = 150

    for degree in range(0, 360, 3):
        x = center_x + radius * math.cos(math.radians(degree))
        y = center_y + radius * math.sin(math.radians(degree))
        draw_character(x, y)

def main():
    """메인 함수 - 세 가지 운동을 무한 반복"""
    print("=== 캐릭터 움직임 무한 반복 시작 ===")
    print("ESC 키를 눌러 종료할 수 있습니다.")

    cycle_count = 0

    while True:
        cycle_count += 1
        print(f"\n--- {cycle_count}번째 사이클 ---")

        # 1. 사각형 운동
        move_rectangle()

        # 2. 삼각형 운동
        move_triangle()

        # 3. 원형 운동
        move_circle()

        # 잠시 대기
        delay(0.5)

# 프로그램 실행
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n프로그램이 종료되었습니다.")
    finally:
        close_canvas()
