.PHONY: all prepare-env clean run_filter run_esteg

all:
	@echo "make prepare-env"
	@echo "    Prepara el entorno."
	@echo "    Se necesita ejecutar con sudo para instalar el manejador de paquetes de Python 3."
	@echo "make clean"
	@echo "    Limpia el proyecto y elimina los archivos generados en el build."
	@echo "make FILTER_ID="" IMG_PATH="" run_filter"
	@echo "    Aplica el filtro seleccionado a la imagen."
	@echo "make MODE="" IMG_PATH="" TXT_PATH="" run_esteg"
	@echo "		Aplica el proceso de estenografía"

prepare-env:
	@if ! [ -x "$(command -v pip3)" ] 2> /dev/null ; then \
		apt update; \
		apt install python3-pip -y ; \
	fi
	@pip3 install -r requirements.txt

clean:
	@rm -rf src/__pycache__ 2> /dev/null || true
	@rm -rf output 2> /dev/null || true

run_filter:
	@cd src && python3 filters.py3 --filter ${FILTER_ID} --img ${IMG_PATH}

run_esteg:
	@if [ ${MODE} = "1" ]; then \
		cd src && python3 steganography.py3 --mode ${MODE} --img ${IMG_PATH} --txt ${TXT_PATH} ; \
	else \
		cd src && python3 steganography.py3 --mode ${MODE} --img ${IMG_PATH} ; \
	fi
