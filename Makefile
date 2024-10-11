##
## Mon Projet Modelisation
## Make
## File description :
## Makefile
##

RM =	rm -f

NAME =	simulation

$(NAME):
	cp src/main.py $@
	chmod +x $@

all: $(NAME)

clean:

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re