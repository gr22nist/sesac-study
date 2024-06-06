const todoInput = document.getElementById('todoInput');
const addBtn = document.getElementById('todoAdd');

//  추가 버튼 마우스 이펙트

addBtn.addEventListener('mouseenter', function() {
    addBtn.classList.add('fa-beat');
});
addBtn.addEventListener('mouseleave', function() {
    addBtn.classList.remove('fa-beat');
});

// 추가 버튼 클릭 시 동작
addBtn.addEventListener('click', function() {
    taskAdd();
});

todoInput.addEventListener('keypress', function(e) {
    enterAdd(e);
});


// 할 일 추가 함수
function taskAdd() {
    if (todoInput.value !== '') {
        //  새로운 항목 생성
        const items = document.createElement('li');
        items.classList.add('todoItem');
        
        //  체크 아이콘 생성
        const checkIco = document.createElement('i');
        checkIco.classList.add('fa-solid', 'fa-check')
        items.appendChild(checkIco)

        // 체크 아이콘 마우스 이펙트
        checkIco.addEventListener('mouseenter', function() {
            checkIco.classList.add('fa-beat', 'hovered')
        });
        checkIco.addEventListener('mouseleave', function() {
            checkIco.classList.remove('fa-beat', 'hovered')
        });
        
        // 아이템 이벤트 리스너
        items.addEventListener('click', function() {
            checkIco.classList.toggle('selected');
            items.classList.toggle('checked')
        });

        //  스팬 태그 생성
        const spanTag = document.createElement('span');
        items.appendChild(spanTag);

        //  텍스트 노드 생성
        const textNode = document.createTextNode(todoInput.value);
        spanTag.appendChild(textNode);

        //  삭제 아이콘 생성
        const delIco = document.createElement('i');
        delIco.classList.add('fa-solid', 'fa-xmark')
        items.appendChild(delIco)

        // 삭제 아이콘 마우스 이펙트
        delIco.addEventListener('mouseenter', function() {
            delIco.classList.add('fa-beat', 'hovered')
        });
        delIco.addEventListener('mouseleave', function() {
            delIco.classList.remove('fa-beat', 'hovered')
        });

        // 삭제 아이콘 클릭시 아이템 삭제
        delIco.addEventListener('click', function() {
            items.remove();
        });
        
        //  새로운 리스트 항목을 HTML에 추가
        document.getElementById('todoList').appendChild(items);

        //  인풋 창 비우기
        todoInput.value = '';
        
    } else {
        alert ('할 일을 입력해주세요!')
    }
}

// 엔터 키 입력 시 동작
function enterAdd(e) {
    const code = e.code;

    if (code === 'Enter') {
        taskAdd();
    }
}