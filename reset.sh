reset(){
    # Pull from repo...
	git pull origin master

    # Delete jobs...
	kubectl delete jobs job-wq-2 setup-wq-2
	
    # Build setup container...
    cd setup
    docker build -t setup-wq-2 .
    docker tag setup-wq-2 197441620132.dkr.ecr.us-west-2.amazonaws.com/setup-wq-2
    docker push 197441620132.dkr.ecr.us-west-2.amazonaws.com/setup-wq-2
    kubectl create -f ./setup.yaml
    sleep 10
    cd ..
    

    pods=$(kubectl describe jobs/setup-wq-2 | grep "Created pod" | sed 's/Normal  SuccessfulCreate.*pod://g')
    podA=$(echo $pods | awk '{print $1}')
    kubectl logs pods/$podA

    docker build -t job-wq-2 .
	docker tag job-wq-2 197441620132.dkr.ecr.us-west-2.amazonaws.com/job-wq-2
	docker push 197441620132.dkr.ecr.us-west-2.amazonaws.com/job-wq-2
	kubectl create -f ./job.yaml
    
    
    sleep 5
	pods=$(kubectl describe jobs/job-wq-2 | grep "Created pod" | sed 's/Normal  SuccessfulCreate.*pod://g')
	podA=$(echo $pods | awk '{print $1}')
    podB=$(echo $pods | awk '{print $2}')
    kubectl logs pods/$podA
    kubectl logs pods/$podB
}
reset