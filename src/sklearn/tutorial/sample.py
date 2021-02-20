from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

def main() -> None:
    X, y = make_classification(random_state=0)
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        random_state=0)
    # print(X_train, y_train)

    pipe = Pipeline([
        ( 'scaler', StandardScaler() ),
        ( 'svc', SVC() )
    ])

    print(pipe)

    # The pipeline can be used as any other estimator
    # and avoids leaking the test set into the train set
    pipe.fit(X_train, y_train)

    print( "\n----- score:" )
    print( "  train score:", pipe.score(X_train, y_train) )
    print( "  test score:",  pipe.score(X_test, y_test) )


if __name__ == '__main__':
    main()
