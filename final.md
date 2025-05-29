# 期末作業

## 習題一

[HW1](https://github.com/yunuun/_sp/blob/main/03c-compiler3/compiler.c)

參考老師給的檔案去修改，有詢問同學要怎麼寫。
```
// DOWHILE = do STMT while (E);
void DOWHILE(){
  int dowhileBegin = nextLabel();
  int dowhileEnd = nextLabel();
  emit("(L%d)\n", dowhileBegin);
  skip("do");
  STMT();
  skip("while");
  skip("(");
  int e = E();
  emit("if not T%d goto L%d\n", e, dowhileEnd);
  skip(")");
  skip(";");
  emit("goto L%d\n", dowhileBegin);
  emit("(L%d)\n", dowhileEnd);
}

```

---

## 習題二

[hw2](https://github.com/yunuun/_sp/tree/main/hw2)
[result](https://github.com/yunuun/_sp/blob/main/hw2/result.md)

參考老師給的檔案去修改
```
int main() // 主程式
{
  int *pc, *bp, *sp, poolsz, *t, *power2, *loc;

  poolsz = 256*1024; // arbitrary size
  if (!(e = malloc(poolsz))) { printf("could not malloc(%d) text area\n", poolsz); return -1; } // 程式段
  if (!(sp = malloc(poolsz))) { printf("could not malloc(%d) stack area\n", poolsz); return -1; }  // 堆疊段

  memset(e, 0, poolsz);


// 3: int power2(int n) {
// 4:   if (n==0) return 1;
  power2 = e;
  *e++ = ENT; *e++ = 0;
  *e++ = LLA; *e++ = 2;
  *e++ = LI;
  *e++ = PSH;
  *e++ = IMM; *e++ = 0;
  *e++ = EQ;
  *e++ = BZ; loc=e; *e++ = 0; 
  *e++ = IMM; *e++ = 1;
  *e++ = LEV;
// 6:   return 2 * power2(n-1);
  *loc = (int) e; *e++ = LLA; *e++ = 2;
  *e++ = LI;
  *e++ = PSH;
  *e++ = IMM; *e++ = 1;
  *e++ = SUB;
  *e++ = PSH;
  *e++ = JSR; *e++ = (int) power2;
  *e++ = ADJ; *e++ = 1;
  *e++ = PSH;
  *e++ = IMM; *e++ = 2;
  *e++ = MUL;
  *e++ = LEV;
// 7: }
//    LEV
  *e++ = LEV;
// 8:
// 9: int main() {
// 10:   printf("power2(3)=%d\n", power2(3));
  pc = e;
  *e++ = ENT; *e++ = 0;
  *e++ = IMM; *e++ = (int) "power2(3)=%d\n";
  *e++ = PSH;
  *e++ = IMM; *e++ = 3;
  *e++ = PSH;
  *e++ = JSR; *e++ = (int) power2;
  *e++ = ADJ; *e++ = 1;
  *e++ = PSH;
  *e++ = PRTF;
  *e++ = ADJ; *e++ = 2;
// 11: }
  *e++ = LEV;

// setup stack
  bp = sp = (int *)((int)sp + poolsz);
  *--sp = EXIT; // call exit if main returns
  *--sp = PSH; t = sp;
  *--sp = (int)t;
  return run(pc, bp, sp);
}
```

---

## 習題三

[hw3](https://github.com/yunuun/_sp/tree/main/hw3/00e-c4for)

參考老師給的檔案去修改，詢問同學要怎麼寫
```
enum { // token : 0-127 直接用該字母表達， 128 以後用代號。
  Num = 128, Fun, Sys, Glo, Loc, Id,
  Char, Else, Enum, If, Int, Return, Sizeof, For, Do, While, 
  Assign, Cond, Lor, Lan, Or, Xor, And, Eq, Ne, Lt, Gt, Le, Ge, Shl, Shr, Add, Sub, Mul, Div, Mod, Inc, Dec, Brak
};
```
```
 else if (tk == Do) {//DoWhile
    next();
    a = e + 1;
    stmt();//先執行一次
    // if (tk == While) next(); else { printf("%d: While expected\n", line); exit(-1); }
    next();
    if (tk == '(') next(); else { printf("%d: open paren expected\n", line); exit(-1); }
    expr(Assign);
    if (tk == ')') next(); else { printf("%d: close paren expected\n", line); exit(-1); }
    if (tk == ';') next(); else { printf("%d: semicolon expected\n", line); exit(-1); }
    *++e = BZ; b = ++e;
    
    *++e = JMP; *++e = (int)a;
    *b = (int)(e + 1);
  }
```
```
   p = "char else enum if int return sizeof for do while "
```

---

## 習題四

[hw3](https://github.com/yunuun/_sp/tree/main/hw4)

參考老師的資料，使用組合語言做出mul3
```
#include <stdio.h>

// 最簡單的版本就是 mul3 函數改用組合語言寫
int mul3(int a, int b, int c);

int main() {
    printf("mul3(3,2,5)=%d\n", mul3(3,2,5));
}
```
```
        .global mul3

        .text
mul3:
        mov %rdi, %rax      
        imulq %rsi, %rax    /* %rax = %rax * %rsi */
        imulq %rdx, %rax    /* %rax = %rax * %rdx */
        ret
```

---

## 習題五

[hw5](https://github.com/yunuun/_sp/blob/main/hw5/power2.md)

參考老師的資料，先編譯再反組譯，md檔的格式有參考同學的


