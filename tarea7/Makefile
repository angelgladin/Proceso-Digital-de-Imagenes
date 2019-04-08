.PHONY: all prepare-env clean run

all:
	@echo "make prepare-env"
	@echo "    Prepara el entorno."
	@echo "    Se necesita ejecutar con sudo para instalar el manejador de paquetes de Python 3."
	@echo "make clean"
	@echo "    Limpia el proyecto y elimina los archivos generados en el build."
	@echo "make FILTER_ID="" IMG_PATH="" run"
	@echo "    Aplica el filtro seleccionado a la imagen."

prepare-env:
	@if ! [ -x "$(command -v pip3)" ] 2> /dev/null ; then \
		apt update; \
		apt install python3-pip -y ; \
	fi
	@pip3 install -r requirements.txt

clean:
	@rm -rf src/__pycache__ 2> /dev/null || true
	@rm -rf output 2> /dev/null || true

run:
	@mkdir output 2> /dev/null || true
	@cd src && python3 filters.py3 --filter ${FILTER_ID} --img ${IMG_PATH}
