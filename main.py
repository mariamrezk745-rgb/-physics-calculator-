print("="*40)
print("⚡ آلة حاسبة فيزياء - قوانين ثانوية عامة ⚡")
print("="*40)
print("1. قانون نيوتن الثاني: F = m * a")
print("2. الطاقة الحركية: KE = 0.5 * m * v^2")
print("3. السرعة: v = d / t")
print("4. قانون أوم: V = I * R")
print("5. الوزن: W = m * g")
print("6. الكثافة: ρ = m / V")
print("7. الضغط: P = F / A")
print("8. قوة الطفو: Fb = ρ * V * g")
print("9. طاقة الوضع: PE = m * g * h")
print("10. القدرة: P = W / t")
print("="*40)

اختيار = input("اختاري رقم القانون 1-10: ")

if اختيار == "1":
    m = float(input("الكتلة m بالكيلو: "))
    a = float(input("العجلة a متر/ث^2: "))
    F = m * a
    print("القوة F =", F, "نيوتن")

elif اختيار == "2":
    m = float(input("الكتلة m بالكيلو: "))
    v = float(input("السرعة v متر/ث: "))
    KE = 0.5 * m * v**2
    print("الطاقة الحركية KE =", KE, "جول")

elif اختيار == "3":
    d = float(input("المسافة d بالمتر: "))
    t = float(input("الزمن t بالثانية: "))
    v = d / t
    print("السرعة v =", v, "متر/ث")

elif اختيار == "4":
    I = float(input("شدة التيار I بالأمبير: "))
    R = float(input("المقاومة R بالأوم: "))
    V = I * R
    print("فرق الجهد V =", V, "فولت")

elif اختيار == "5":
    m = float(input("الكتلة m بالكيلو: "))
    g = 9.8
    W = m * g
    print("الوزن W =", W, "نيوتن")

elif اختيار == "6":
    m = float(input("الكتلة m بالكيلو: "))
    V = float(input("الحجم V متر^3: "))
    p = m / V
    print("الكثافة ρ =", p, "كجم/م^3")

elif اختيار == "7":
    F = float(input("القوة F نيوتن: "))
    A = float(input("المساحة A متر^2: "))
    P = F / A
    print("الضغط P =", P, "باسكال")

elif اختيار == "8":
    p = float(input("كثافة السائل ρ كجم/م^3: "))
    V = float(input("حجم الجسم المغمور V متر^3: "))
    g = 9.8
    Fb = p * V * g
    print("قوة الطفو Fb =", Fb, "نيوتن")

elif اختيار == "9":
    m = float(input("الكتلة m بالكيلو: "))
    h = float(input("الارتفاع h بالمتر: "))
    g = 9.8
    PE = m * g * h
    print("طاقة الوضع PE =", PE, "جول")

elif اختيار == "10":
    W = float(input("الشغل W بالجول: "))
    t = float(input("الزمن t بالثانية: "))
    P = W / t
    print("القدرة P =", P, "وات")

else:
    print("رقم غير صحيح! اختاري من 1 لـ 10")