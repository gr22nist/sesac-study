// 엘리먼트 및 속성 추가
function createElementWithAttributes(tag, attributes) {
    let element = document.createElement(tag);
    Object.keys(attributes).forEach((key) => {
        element.setAttribute(key, attributes[key]);
    });
    return element;
}

//부모 엘리먼트에 자식 추가
function appendToParent(parent, child) {
    document.getElementById(parent).appendChild(child);
}

// 아이템에 이벤트리스너 추가
function addItemListeners(item, checkBtn, delBtn) {
    //  체크 아이콘 클릭 시 토글기능
    checkBtn.addEventListener("click", function () {
        checkBtn.classList.toggle('seleted')
        item.classList.toggle('checked')
    });

    // 삭제 버튼 호버 시 이펙트 부여
    delBtn.addEventListener("mouseenter", function () {
        delBtn.classList.add("fa-beat-fade", "hovered");
    });

    delBtn.addEventListener("mouseleave", function () {
        delBtn.classList.remove("fa-beat-fade", "hovered");
    });
    // 삭제 버튼 클릭 시 아이템 삭제
    delBtn.addEventListener("click", function () {
        item.remove();
    });
};

//  추가 버튼 클릭 시 동작
document.getElementById('todoAdd').addEventListener("click", function () {
    const todoInput = document.getElementById("todoInput");
    //  입력 필드에서 값 가져오기
    const todoInputValue = todoInput.value;

    if (todoInputValue !== "") {
        //  뉴 항목 생성
        const newItem = createElementWithAttributes("li", {
        id: "todoItem"
        });
        //  투두 항목 생성 시, 체크아이콘 포함
        const checkBtn = createElementWithAttributes("i", {
        id: "todoCheck",
        class: "fa-solid fa-check",
        });
        appendToParent(newItem, checkBtn);
        //  텍스트 노드 생성
        const newNode = document.createTextNode(todoInputValue);
        appendToParent(newItem, newNode);

        //  삭제 버튼 생성 및 클래스 추가
        const delBtn = createElementWithAttributes("i", {
        class: "fa-solid fa-xmark",
        });
        appendToParent(newItem, delBtn);

        //  새로운 리스트 항목을 HTML에 추가
        appendToParent("todoList", newItem);

        //  인풋 창 비우기
        todoInput.value = "";

        //  이벤트 리스너 추가
        addItemListeners(newItem, checkBtn, delBtn);
    
    } else {
        alert("할 일을 입력해주세요!");
    }
});
