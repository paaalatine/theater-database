python2 basic_operations.py service create wardrobe
python2 basic_operations.py service create stage
python2 basic_operations.py service create buffet
python2 basic_operations.py service create cashbox
python2 basic_operations.py service read
echo "============================================"

python2 basic_operations.py post create wardrobber 25000 1
python2 basic_operations.py post create stagecleaner 30000 2
python2 basic_operations.py post create saller 30000 3
python2 basic_operations.py post create cashboxer 45000 4
python2 basic_operations.py post read
echo "============================================"

#python2 basic_operations.py staff create Valentina 1
#python2 basic_operations.py staff create Petr 1
#python2 basic_operations.py staff create Oleg 2
#python2 basic_operations.py staff create Gennady 3
#python2 basic_operations.py staff create Olga 4
#python2 basic_operations.py staff read
#echo "============================================"

python2 basic_operations.py performance create Athello 3000 wooow
python2 basic_operations.py performance create Snegurochka 3500 coolstory
python2 basic_operations.py performance create Romario\ and\ Dakotta 4000 unbelievable
python2 basic_operations.py performance read
echo "============================================"

python2 basic_operations.py requisite create brains 400
python2 basic_operations.py requisite create chair 500
python2 basic_operations.py requisite create bottle 500
python2 basic_operations.py requisite create brains 400
python2 basic_operations.py requisite read
echo "============================================"

