@bp.route("reviews")
def reviews():
    # this block checks if the current user has any reviews saved
    check_reviews = Reviews.query.filter_by(user_id=current_user.id).first()
    # if no, the page will tell them they don't have any review saved and will suggest for them to save one.
    if check_reviews == None:
        

        return render_template(
            "index.html",
            current_user=current_user.username,
            has_reviews=has_reviews,
        )
    # if yes, one of the reviews are chosen randomly and its movie id is used in the API, and the returned data will be displayed to the user
    else:

        reviews = Reviews.query.filter_by(user_id=current_user.id).all()
        i = randrange(len(reviews))
        movie_id = reviews[i].movie_id
        other_data = get_movie_info(movie_id)
    
    else:
        return render_template("error.html")
