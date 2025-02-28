import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title('简单计算器')
    
    # 输入数字
    num1 = st.number_input('请输入第一个数字', value=0.0)
    num2 = st.number_input('请输入第二个数字', value=0.0)
    
    # 选择运算符
    operation = st.selectbox(
        '选择运算符',
        ('+', '-', '*', '/')
    )
    
    # 计算结果
    if st.button('计算'):
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/' and num2 != 0:
            result = num1 / num2
        else:
            result = '错误：除数不能为0'
        
        st.success(f'计算结果: {result}')

    # 添加HTML计算器
    st.markdown("---")
    st.subheader('HTML版计算器')
    with open('streamlit_html/calculator.html', 'r', encoding='utf-8') as file:
        calculator_html = file.read()
    components.html(calculator_html, height=600)

if __name__ == '__main__':
    main()