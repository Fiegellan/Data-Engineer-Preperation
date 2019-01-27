def estimate_square(square, estimate,episolon):
        y = (estimate + (square/estimate))/2
        print y
        # if abs(y-estimate) < episolon:
        #     print y
        # else:
        #     estimate_square(square,y,episolon)
        while abs(y-estimate) > episolon:
            estimate_square(square, y, episolon)

        print y

estimate_square(100,100,0.0000001)