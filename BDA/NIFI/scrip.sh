USUARIO="xuedua095"
# Copiar a hadoop.cesga.es
echo "LLegué antes del scp" >> /tmp/log.txt
scp /home/cesgaxuser/nifi-compartido/datasets/meteogalicia-junto/*.csv ${USUARIO}@hadoop.cesga.es:/home/xunta/edu/a095/meteogal
echo "LLegué después del scp" >> /tmp/log.txt
# Subir al HDFS
echo "LLegué antes del ssh" >> /tmp/log.txt
ssh ${USUARIO}@hadoop.cesga.es hdfs dfs -put /home/xunta/edu/a095/meteogal/
echo "LLegué después del ssh" >> /tmp/log.txt