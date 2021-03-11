
@ECHO OFF

REM ============================================================================

SET CREATE_DATE=%date:-=%
SET CREATE_TIME=%time::=%

SET SOURCE=C:\Users\Administrator\PycharmProjects
SET TARGET=C:\▶02.기타\99.소스빽업\%CREATE_DATE%_%CREATE_TIME:.=%

ECHO CREATE_DATE = %CREATE_DATE%
ECHO CREATE_TIME = %CREATE_TIME%
ECHO.
ECHO SOURCE = %SOURCE%
ECHO TARGET = %TARGET%

REM PAUSE>NUL

REM ============================================================================

:: 빽업폴더가 있는경우 삭제
::IF EXIST %TARGET% (
::	RMDIR /S /Q %TARGET%
::	ECHO ■■■기존 빽업폴더가 삭제되었습니다.
::)

REM MKDIR %TARGET%

XCOPY "%SOURCE%" "%TARGET%\*" /s /h /e /y /exclude:.\exclude-list.txt

ECHO.
ECHO ■■■빽업이 완료되었습니다.


