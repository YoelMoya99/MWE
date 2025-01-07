c:
	gcc -o test_c Maquina_Estado_C.c
	./test_c

cpp:
	g++ -o test_cpp Maquina_Estado_Cpp.cpp
	./test_cpp

clean_c:
	rm test_c

clean_cpp:
	rm test_cpp
