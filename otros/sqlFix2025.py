comandoSQL = r"""

@echo off
cls
COLOR 0E
set maquina=%COMPUTERNAME%
echo Configurando SQL DEVELOPER en Maquina: %maquina%


echo SID_LIST_LISTENER = > C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo   (SID_LIST = >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo    (SID_DESC = >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo      (SID_NAME = PLSExtProc) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo      (ORACLE_HOME = C:\oraclexe\app\oracle\product\11.2.0\server) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo      (PROGRAM = extproc) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo    ) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo    (SID_DESC = >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo      (SID_NAME = CLRExtProc) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo      (ORACLE_HOME = C:\oraclexe\app\oracle\product\11.2.0\server) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo      (PROGRAM = extproc) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo    ) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo  ) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo LISTENER = >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo   (DESCRIPTION_LIST = >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo     (DESCRIPTION = >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo       (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1)) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo       (ADDRESS = (PROTOCOL = TCP)(HOST = %maquina%)(PORT = 1521)) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo     ) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo   ) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora
echo DEFAULT_SERVICE_LISTENER = (XE) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\listener.ora

echo OK - LISTENER.ORA!

echo XE = > C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo   (DESCRIPTION = >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo     (ADDRESS = (PROTOCOL = TCP)(HOST = %maquina%)(PORT = 1521)) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo     (CONNECT_DATA = >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo       (SERVER = DEDICATED) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo       (SERVICE_NAME = XE) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo     ) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo   ) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo EXTPROC_CONNECTION_DATA = >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo   (DESCRIPTION = >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo     (ADDRESS_LIST = >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo       (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1)) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo     ) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo     (CONNECT_DATA = >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo       (SID = PLSExtProc) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo       (PRESENTATION = RO) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo     ) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo   ) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo ORACLR_CONNECTION_DATA = >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo   (DESCRIPTION =  >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo     (ADDRESS_LIST =  >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo       (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1)) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo     ) >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo     (CONNECT_DATA =  >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo       (SID = CLRExtProc)  >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo       (PRESENTATION = RO)  >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo     )  >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora
echo   )  >> C:\app\Laboratorio\product\21c\homes\OraDB21Home1\network\admin\tnsnames.ora

echo OK - TNSNAMES.ORA!
echo OracleXE Reparado Exitosamente!
echo .......................................................
echo 1: Vuelva a iniciar la Base de Datos con Start Database
echo 2: Con ctese a la Base de Datos
echo .......................................................
echo Fix Developer hecho por Kevin Rojas
echo
quit

"""

print(comandoSQL.replace("Laboratorio", "Informatica"))
