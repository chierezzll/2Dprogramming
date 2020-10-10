# 게임의 소개
- 죽림고수
- copy게임이며 원 게임은 플래시 게임입니다.
- 사방에서 화살이 날라오면 그 화살들을 피해 최대한 오래 버티는 게임입니다. 
- wasd 나 방향키를 사용하여 움직이면 된다.

<
![죽림1](https://user-images.githubusercontent.com/70653452/94156102-a7c06f00-feba-11ea-91d8-fdcb54d4ef01.PNG)
![죽림2](https://user-images.githubusercontent.com/70653452/94156116-aa22c900-feba-11ea-83de-24af7ee4ea11.PNG)
![죽림3](https://user-images.githubusercontent.com/70653452/94156120-aabb5f80-feba-11ea-88e4-d193c76266ab.PNG)
>

# GameState 의 수 및 각각의 이름
1. Logo_state
2. Title_state
3. Game_state
4. Gameover_state
5. Score_state

# 각 Gamestate 별 다음 항목
1. Logo_state 
 로고가 나오고 1초후에 자동으로 타이틀 화면으로 전환한다.
 escape키를 누르면 게임은 종료된다. 

2. Title_state
 타이틀화면이 나오면 게임시작, 점수보기, 게임종료 3가지의 동작을 선택할 수 있다.
 게임시작을 누르면 game_state으로 넘어간다.
 점수보기를 누르면 score_state으로 넘어간다.
 게임종료를 누르면 게임이 종료된다.

3. Game_state  
 게임이 시작되고 사방에서 화살이 한 두개씩 나오다가 시간이 지날수록 나오는 개수가 많아진다. 화살의 방향은 제각각이며 속도는 일정하다. 
 객체목록 - 화살, 주인공
 화살에 부딪히게 되면 Gameover_state으로 넘어간다.

4. Gameover_state
 화살에 부딪혔을때만 나오며 점수를 보여준다. 처음으로, 점수등록 중 하나를 선택할 수 있다.
처음으로를 누르면 Title_state으로 돌아간다.
점수등록을 누르면 Score_state으로 넘어간다.  

5. Score_state
 점수를 등록하는 곳이며 사용자에게 문자를 입력받아 자신의 이름을 등록할 수 있다. 
등록하기를 마치면 Title_state으로 돌아간다. 

![다이어그램1](https://user-images.githubusercontent.com/70653452/95652667-b3a06800-0b2d-11eb-973c-d64b85334d2d.PNG)
# 필요한 기술
 주인공은 wasd나 방향키를 입력받아 움직인다.
 시간이 지남에 따라 화살의 수가 증가해야하는 기술이 필요,
 또 랜덤한 위치에서 화살이 날라와야 하므로 랜덤함수를 쓸 필요가 있음.
 
 
 
 #개발범위
 ![개발범위](https://user-images.githubusercontent.com/70653452/95652650-94a1d600-0b2d-11eb-8c60-929ad8dbc3c9.PNG)
 
 #개발계획
 ![개발계획](https://user-images.githubusercontent.com/70653452/95652652-966b9980-0b2d-11eb-8879-ddd9500cc8e9.PNG)
